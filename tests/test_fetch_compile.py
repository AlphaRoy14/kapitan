import os
import sys
import tempfile
import unittest
from kapitan.cli import main
from shutil import rmtree
from distutils.dir_util import copy_tree
from kapitan.cached import reset_cache


class TestJustOneFunc(unittest.TestCase):

    def test_compile_fetch_classes_that_doesnot_exist_yet(self):
        """
        runs $ kapitan compile --fetch --search-paths temp_dir --output-path temp_dir --inventory-path temp_dir/inventory -t monitoring-dev
        The `monitor` class does not exist initially, it is fetched and then compiled
        """
        os.chdir(
            os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "test_remote_inventory", "environment_three"
            )
        )
        temp_dir = tempfile.mkdtemp()
        # copying helm_values_files to the search path
        sys.argv = [
            "kapitan",
            "compile",
            "--fetch",
            "--search-paths",
            temp_dir,
            "--output-path",
            temp_dir,
            "-t",
            "monitoring-dev",
        ]
        main()
        self.assertTrue(os.path.isdir(os.path.join(temp_dir, "charts", "prometheus")))
        rmtree(temp_dir)
        reset_cache()