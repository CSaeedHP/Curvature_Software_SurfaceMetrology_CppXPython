#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include "Processor.h"

namespace py = pybind11;

PYBIND11_MODULE(curvature, m) {
    m.doc() = "Curvature analysis module exposed via pybind11";

    py::class_<Processor>(m, "Processor")
        .def(py::init<>())  // constructor
        .def("loadData", &Processor::loadData,
             py::arg("inputfile"),
             py::arg("minscale"),
             py::arg("maxscale"),
             py::arg("hybrid"),
             py::arg("acutemethod"),
             py::arg("obtusemethod"),
             "Load data from a file and set processing parameters")
        .def("processData", &Processor::processData,
             "Process the loaded data")
        .def("writeData", &Processor::writeData,
             py::arg("filePath"),
             "Write processed data to a file")
        .def("fetchData", &Processor::fetchData,
             "Return the processed data as a NumPy array");
}
