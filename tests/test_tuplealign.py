import unittest
from tuplealign.alignment import aligned_tuples_to_MSA

input_data1 = [
    ["a-bcdef", "aAb----"],
    ["a-bcdef", "-Bbc-ef"],
    ["abcde-f-", "---deEfF"]
]

input_data2 = [
    [
        "Today I w-oke up and went to my friend Manu's house for lunch",
        "Today I stood up---------------------------------------------"
    ],
    [
        "Today I woke up and went to my friend Manu--'s house for lunch",
        "----------------------------my friend Cassie's house----------"
    ]
]

input_data3 = [["ata---", "ataaaa"], ["---ata", "aaaaca"]]

# Same but adding flanking gaps in the first one only (a gap is kept in all in the MSA, but only at the end)
input_data4 = [["-ata----", "-ataaaa-"], ["---ata", "aaaaca"]]

# Flanking gaps in both (flanking gaps are present in the MSA as well on both start and end)
input_data5 = [["-ata----", "-ataaaa-"], ["----ata-", "-aaaaca-"]]


class TestTuplesToMSA(unittest.TestCase):
    def test_aligned_tuples_to_MSA_1(self):
        result1 = aligned_tuples_to_MSA(input_data1)
        expected1 = ["A-BCDE-F-", "AAB------", "-BBC-E-F-", "----DEEFF"]
        self.assertEqual(result1, expected1)

    def test_aligned_tuples_to_MSA_2(self):
        result1 = aligned_tuples_to_MSA(input_data2)
        expected1 = [
            "TODAY I W-OKE UP AND WENT TO MY FRIEND MANU--'S HOUSE FOR LUNCH",
            "TODAY I STOOD UP-----------------------------------------------",
            "-----------------------------MY FRIEND CASSIE'S HOUSE----------",
        ]
        self.assertEqual(result1, expected1)

    def test_aligned_tuples_to_MSA_3(self):
        result3 = aligned_tuples_to_MSA(input_data3)
        expected3 = ["---ATA---", "---ATAAAA", "AAAACA---"]
        self.assertEqual(result3, expected3)

    def test_aligned_tuples_to_MSA_4(self):
        result4 = aligned_tuples_to_MSA(input_data4)
        expected4 = ["---ATA----", "---ATAAAA-", "AAAACA----"]
        self.assertEqual(result4, expected4)

    def test_aligned_tuples_to_MSA_5(self):
        result5 = aligned_tuples_to_MSA(input_data5)
        expected5 = ["----ATA----", "----ATAAAA-", "-AAAACA----"]
        self.assertEqual(result5, expected5)


if __name__ == "__main__":
    unittest.main()

