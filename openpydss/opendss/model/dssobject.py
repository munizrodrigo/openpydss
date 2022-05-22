import py_dss_interface
from glob import glob
from pathlib import PurePath
from importlib import import_module
from inspect import getmembers, isclass, getfile
from os.path import basename, dirname, join, abspath, splitext


INDENT_STR = "    "


class DSSObject(object):
    dss = py_dss_interface.DSSDLL()

    dss_properties_invalid_exp = {
        "class": "Class",
        "%": "pct_",
        "-": "_x_"
    }

    def __init__(self):
        pass

    @classmethod
    def get_classes(cls):
        current_dir = join(dirname(abspath(__file__)))
        module_name = ".".join(PurePath(current_dir).parts[-3:])

        classes_list = []
        for file in glob(join(current_dir, "*.py")):
            name = splitext(basename(file))[0]

            if name.startswith("__") or name == "dssobject":
                continue

            module = import_module(f"{module_name}.{name}")

            clsmembers = getmembers(module, isclass)
            clsmembers = [clsmember[1] for clsmember in clsmembers if not clsmember[0] == "DSSObject"]
            classes_list.extend(clsmembers)

        return classes_list

    @classmethod
    def get_class_dss_properties(cls, cls_name):
        cls.dss.dss_clear_all()
        cls.dss.dss_new_circuit("circuit")
        cls.dss.text(f"new {cls_name}.{cls_name}")
        dss_properties = {name: index + 1 for index, name in enumerate(cls.dss.cktelement_all_property_names())}
        return dss_properties

    @classmethod
    def generate_stub(cls):
        dss_classes = cls.get_classes()

        for dss_class in dss_classes:
            cls_name = dss_class.__name__
            filename = basename(getfile(dss_class)).split(".")[0]
            filepath = join(dirname(__file__), f"{filename}.pyi")

            dss_properties = cls.get_class_dss_properties(cls_name=cls_name)

            pyi_str = f"class {cls_name}:\n"

            for name, index in dss_properties.items():
                corrected_name = name
                for invalid_exp, valid_exp in cls.dss_properties_invalid_exp.items():
                    corrected_name = corrected_name.replace(invalid_exp, valid_exp)

                property_default_value = cls.dss.dssproperties_read_value(str(index))
                pyi_str += f"{INDENT_STR}{corrected_name} = \"{property_default_value}\"  # type: str\n"

            with open(filepath, "w") as pyi_file:
                pyi_file.write(pyi_str)

    @classmethod
    def generate_classes(cls, generate_stub=True):
        dss_classes = cls.get_classes()

        for dss_class in dss_classes:
            cls_name = dss_class.__name__
            filename = basename(getfile(dss_class)).split(".")[0]
            filepath = join(dirname(__file__), f"{filename}.py")

            dss_properties = cls.get_class_dss_properties(cls_name=cls_name)

            py_str = "from openpydss.opendss.model.dssobject import DSSObject\n\n\n"
            py_str += f"class {cls_name}(DSSObject):\n"
            py_str += f"{INDENT_STR}def __init__(\n"
            py_str += f"{INDENT_STR}{INDENT_STR}{INDENT_STR}self,\n"

            for name, index in dss_properties.items():
                corrected_name = name
                for invalid_exp, valid_exp in cls.dss_properties_invalid_exp.items():
                    corrected_name = corrected_name.replace(invalid_exp, valid_exp)

                property_default_value = cls.dss.dssproperties_read_value(str(index))

                py_str += f"{INDENT_STR}{INDENT_STR}{INDENT_STR}{corrected_name}=\"{property_default_value}\",\n"

            py_str += f"{INDENT_STR}):\n"
            py_str += f"{INDENT_STR}{INDENT_STR}super().__init__()\n"

            for name, index in dss_properties.items():
                corrected_name = name
                for invalid_exp, valid_exp in cls.dss_properties_invalid_exp.items():
                    corrected_name = corrected_name.replace(invalid_exp, valid_exp)

                py_str += f"{INDENT_STR}{INDENT_STR}self.{corrected_name} = {corrected_name}\n"

            with open(filepath, "w") as py_file:
                py_file.write(py_str)

        if generate_stub:
            cls.generate_stub()
