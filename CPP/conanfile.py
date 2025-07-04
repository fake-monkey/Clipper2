from conan import ConanFile
from conan.tools import cmake
from conan.tools.cmake import CMakeToolchain
from os import path
from pathlib import Path
from conan.tools import files

class Clipper2Recipe(ConanFile):
    name = "clipper2"
    version = "1.5.4"
    user = "third_party"
    channel = "stable"

    settings = "os", "arch"

    def package(self):
        files.copy(self, "*", self.source_folder, self.package_folder, keep_path=True)

    def package_info(self):
        self.cpp_info.builddirs = ["cmake/clipper2"]
        self.cpp_info.set_property("cmake_find_mode", "none")
