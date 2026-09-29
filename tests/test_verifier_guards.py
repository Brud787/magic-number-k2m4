"""Engineering safeguards: corrupt certificates must be rejected."""
import copy
import importlib.util
from pathlib import Path
import subprocess
import sys
import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from verifier.exact import determinant, rank_certificate
from verifier import checks


def test_empty_minor_convention():
    assert determinant([])==1
    assert rank_certificate([],1,[],[],[],1)==0


def test_lower_bound_without_upper_bound_is_rejected():
    with pytest.raises(AssertionError):
        rank_certificate([[1,0],[0,1]],2,[0],[0],[[(0,'1')]],1)


def test_bad_minor_is_rejected():
    with pytest.raises(AssertionError):
        rank_certificate([[1,0],[0,1]],2,[0,1],[0,1],[[(0,'1')],[(1,'1')]],-1)


def test_membership_catalogue_tamper(monkeypatch):
    original=checks.read
    def tampered(path):
        data=original(path)
        if path=='membership/catalogue.json':
            data['cells'][0]['membership_status']='CERTIFIED_NON_TILE'
        return data
    monkeypatch.setattr(checks,'read',tampered)
    with pytest.raises(AssertionError):checks.membership_catalogue()


def test_optimized_python_is_refused():
    result=subprocess.run([sys.executable,'-O',str(Path(__file__).resolve().parents[1]/'verify_all.py'),'--certificate','MEM-CORES'],capture_output=True,text=True)
    assert result.returncode!=0 and 'requires assertions' in result.stderr


def test_unknown_certificate_id_is_refused():
    result=subprocess.run([sys.executable,str(Path(__file__).resolve().parents[1]/'verify_all.py'),'--certificate','NONEXISTENT'],capture_output=True,text=True)
    assert result.returncode!=0 and 'invalid choice' in result.stderr
