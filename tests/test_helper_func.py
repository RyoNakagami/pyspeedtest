import sys
from pathlib import Path
import builtins
import pytest
from library.helper_func import get_version

def test_get_version_real_file():
    # 実際の pyproject.toml が存在する前提で呼び出し
    version = get_version()
    assert isinstance(version, str)
    assert len(version.split(".")) >= 3  # e.g., "0.1.0"

def test_get_version_file_not_exist(monkeypatch):
    # Path.exists を False にモック
    monkeypatch.setattr(Path, "exists", lambda self: False)
    version = get_version()
    assert version == "0.0.0"

def test_get_version_broken_file(tmp_path, monkeypatch):
    # 一時ファイルで壊れた toml を作成
    broken_file = tmp_path / "pyproject.toml"
    broken_file.write_text("not-a-toml")

    # Path.parents[2] を tmp_path に差し替える
    class FakePath(Path):
        def __new__(cls, *args, **kwargs):
            return Path(*args, **kwargs)
        @property
        def parents(self):
            class Parents:
                def __getitem__(self_inner, idx):
                    return tmp_path
            return Parents()

    monkeypatch.setattr("library.helper_func.Path", FakePath)
    version = get_version()
    assert version == "0.0.0"
