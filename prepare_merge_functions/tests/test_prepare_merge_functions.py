import unittest
import pandas as pd
import tempfile
import os
from radar_utils.prepare_merge_functions import prepare_sequence_data, merge_label_ids


class TestSequenceDataPreparation(unittest.TestCase):

    def setUp(self):
        # Temporäre Daten für die Tests erstellen
        self.temp_dir = tempfile.TemporaryDirectory()

        # Beispiel-Datenframes erstellen
        self.df1 = pd.DataFrame({
            'label_id': [0, 5, 11, 99],
            'feature1': [1, 2, 3, 4],
            'feature2': [5, 6, None, 8]
        })

        self.df2 = pd.DataFrame({
            'label_id': [7, 8, 1],
            'feature1': [9, 10, 11],
            'feature2': [12, 13, 14]
        })

        # Speichern der Dataframes als Pickle-Dateien
        self.df1.to_pickle(os.path.join(self.temp_dir.name, "data1.pkl"))
        self.df2.to_pickle(os.path.join(self.temp_dir.name, "data2.pkl"))

    def tearDown(self):
        # Temporäre Dateien nach Abschluss der Tests löschen
        self.temp_dir.cleanup()

    def test_merge_label_ids(self):
        # Testet die Funktion merge_label_ids
        df_test = pd.DataFrame({
            'label_id': [0, 6, 7, 11, 50, None]
        })
        result = merge_label_ids(df_test)

        expected_labels = ["CAR", "TWO_WHEELER", "OTHER", "PEDESTRIAN", "PEDESTRIAN", "CAR"]




        self.assertListEqual(result['label_id'].tolist(), expected_labels)

    def test_prepare_sequence_data(self):
        # Testet die Funktion prepare_sequence_data
        result_df = prepare_sequence_data(self.temp_dir.name, drop_features=['feature2'])

        # Prüfen auf Entfernung von NaN-Werten
        self.assertFalse(result_df.isna().any().any())

        # Prüfen, ob 'feature2' entfernt wurde
        self.assertNotIn('feature2', result_df.columns)

        # Prüfen, ob Daten richtig zusammengeführt wurden
        self.assertEqual(len(result_df), 6)

        # Prüfen, ob 'label_id' korrekt konvertiert wurde
        expected_labels = ["CAR", "TWO_WHEELER", "OTHER", "PEDESTRIAN", "PEDESTRIAN", "CAR"]





        self.assertListEqual(result_df['label_id'].tolist(), expected_labels)

        # Ausgabe der Ergebnisse zur Kontrolle
        print(result_df)


if __name__ == '__main__':
    unittest.main()





#pytest --cov=radar_utils --cov-report=term-missing -q
