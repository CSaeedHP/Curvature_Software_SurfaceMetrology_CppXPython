#include <pybind11/pybind11.h>
#include <Processor.h>
namespace py = pybind11;

//creates a module in python called "polycurve"
PYBIND11_MODULE(Polycurve, m) {
    //adds a class "greeter, called as polycurve.Greeter"
    py::class_<Processor>(m, "Processor")
        //adds the constructor
        .def(py::init<const std::string &>())
        //creates the binding for Greeter
        .def("greet", &Greeter::greet);
}

