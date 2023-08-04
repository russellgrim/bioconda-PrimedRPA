import pytest
from PrimedRPA import *

def test_assert_True():
    assert return_true()

def test_FastaToDict():
    fasta_dic = FastaToDict("Validation/Validation_1_Input.fasta")
    assert fasta_dic["Seq1"][0] == "G"