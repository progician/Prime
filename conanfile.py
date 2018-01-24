from conans import ConanFile, CMake

class PrimeConan(ConanFile):
    name = "Prime"
    version = "1.0.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "Library with prime test in it"
    url = "None"
    license = "None"
    generators = [ "cmake" ]

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*.a", dst="lib", keep_path=False)
        self.copy(pattern="*.cmake", dst="cmake", src="CMakeFiles/Export", keep_path=False)
        self.copy(pattern="PrimeConfig.cmake", dst="cmake", keep_path=False)
        self.copy(pattern="PrimeConfigVersion.cmake", dst="cmake", keep_path=False)
        self.copy(pattern="*", dst="include", src="include")
    
    def package_info(self):
        self.cpp_info.libs = [ "Prime" ] 
