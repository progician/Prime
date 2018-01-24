Prime Library
=============

Simple library that is used as a test case for the conan workflow. Nothing fancy, a single static library with a single function for prime testing. The point here is to test how can a well formed CMake project work along with the cmake workflow.


Build
-----

The building of the library is trivial in terms of CMake

1. Clone the repository: `$ git clone https://github.com/progician/Prime.git` 
2. Create a build directory, like: `$ cd Prime && mkdir build && cd build`
3. Configure the project `$ cmake .. -GNinja`
4. Run the build `ninja`
5. Package using ninja: `ninja package`

However, more interesing is how you would do it, when using *conan*

1. Clone the repository: `$ git clone https://github.com/progician/Prime.git` 
2. Step into the build directory `$ cd Prime`
3. Initialise the build directory and the conan cmake information: `$ conan install -if build .`
4. Run the build: `$ CONAN_CMAKE_GENERATOR=Ninja conan build -bf build .`
5. Package: `$ conan package -bf build .`
6. Export the package to your local conan cache `conan export-pkg -bf build . Prime/[VERSION]@USER/CHANNEL

At the end of these steps the Prime library should be ready to use in your local conan cache. Which means that you can add this library as a dependency to your project.
