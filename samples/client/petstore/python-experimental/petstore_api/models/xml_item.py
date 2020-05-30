# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401
import nulltype  # noqa: F401

from petstore_api.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)


class XmlItem(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'attribute_string': (str,),  # noqa: E501
            'attribute_number': (float,),  # noqa: E501
            'attribute_integer': (int,),  # noqa: E501
            'attribute_boolean': (bool,),  # noqa: E501
            'wrapped_array': ([int],),  # noqa: E501
            'name_string': (str,),  # noqa: E501
            'name_number': (float,),  # noqa: E501
            'name_integer': (int,),  # noqa: E501
            'name_boolean': (bool,),  # noqa: E501
            'name_array': ([int],),  # noqa: E501
            'name_wrapped_array': ([int],),  # noqa: E501
            'prefix_string': (str,),  # noqa: E501
            'prefix_number': (float,),  # noqa: E501
            'prefix_integer': (int,),  # noqa: E501
            'prefix_boolean': (bool,),  # noqa: E501
            'prefix_array': ([int],),  # noqa: E501
            'prefix_wrapped_array': ([int],),  # noqa: E501
            'namespace_string': (str,),  # noqa: E501
            'namespace_number': (float,),  # noqa: E501
            'namespace_integer': (int,),  # noqa: E501
            'namespace_boolean': (bool,),  # noqa: E501
            'namespace_array': ([int],),  # noqa: E501
            'namespace_wrapped_array': ([int],),  # noqa: E501
            'prefix_ns_string': (str,),  # noqa: E501
            'prefix_ns_number': (float,),  # noqa: E501
            'prefix_ns_integer': (int,),  # noqa: E501
            'prefix_ns_boolean': (bool,),  # noqa: E501
            'prefix_ns_array': ([int],),  # noqa: E501
            'prefix_ns_wrapped_array': ([int],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        'attribute_string': 'attribute_string',  # noqa: E501
        'attribute_number': 'attribute_number',  # noqa: E501
        'attribute_integer': 'attribute_integer',  # noqa: E501
        'attribute_boolean': 'attribute_boolean',  # noqa: E501
        'wrapped_array': 'wrapped_array',  # noqa: E501
        'name_string': 'name_string',  # noqa: E501
        'name_number': 'name_number',  # noqa: E501
        'name_integer': 'name_integer',  # noqa: E501
        'name_boolean': 'name_boolean',  # noqa: E501
        'name_array': 'name_array',  # noqa: E501
        'name_wrapped_array': 'name_wrapped_array',  # noqa: E501
        'prefix_string': 'prefix_string',  # noqa: E501
        'prefix_number': 'prefix_number',  # noqa: E501
        'prefix_integer': 'prefix_integer',  # noqa: E501
        'prefix_boolean': 'prefix_boolean',  # noqa: E501
        'prefix_array': 'prefix_array',  # noqa: E501
        'prefix_wrapped_array': 'prefix_wrapped_array',  # noqa: E501
        'namespace_string': 'namespace_string',  # noqa: E501
        'namespace_number': 'namespace_number',  # noqa: E501
        'namespace_integer': 'namespace_integer',  # noqa: E501
        'namespace_boolean': 'namespace_boolean',  # noqa: E501
        'namespace_array': 'namespace_array',  # noqa: E501
        'namespace_wrapped_array': 'namespace_wrapped_array',  # noqa: E501
        'prefix_ns_string': 'prefix_ns_string',  # noqa: E501
        'prefix_ns_number': 'prefix_ns_number',  # noqa: E501
        'prefix_ns_integer': 'prefix_ns_integer',  # noqa: E501
        'prefix_ns_boolean': 'prefix_ns_boolean',  # noqa: E501
        'prefix_ns_array': 'prefix_ns_array',  # noqa: E501
        'prefix_ns_wrapped_array': 'prefix_ns_wrapped_array',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """xml_item.XmlItem - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            attribute_string (str): [optional]  # noqa: E501
            attribute_number (float): [optional]  # noqa: E501
            attribute_integer (int): [optional]  # noqa: E501
            attribute_boolean (bool): [optional]  # noqa: E501
            wrapped_array ([int]): [optional]  # noqa: E501
            name_string (str): [optional]  # noqa: E501
            name_number (float): [optional]  # noqa: E501
            name_integer (int): [optional]  # noqa: E501
            name_boolean (bool): [optional]  # noqa: E501
            name_array ([int]): [optional]  # noqa: E501
            name_wrapped_array ([int]): [optional]  # noqa: E501
            prefix_string (str): [optional]  # noqa: E501
            prefix_number (float): [optional]  # noqa: E501
            prefix_integer (int): [optional]  # noqa: E501
            prefix_boolean (bool): [optional]  # noqa: E501
            prefix_array ([int]): [optional]  # noqa: E501
            prefix_wrapped_array ([int]): [optional]  # noqa: E501
            namespace_string (str): [optional]  # noqa: E501
            namespace_number (float): [optional]  # noqa: E501
            namespace_integer (int): [optional]  # noqa: E501
            namespace_boolean (bool): [optional]  # noqa: E501
            namespace_array ([int]): [optional]  # noqa: E501
            namespace_wrapped_array ([int]): [optional]  # noqa: E501
            prefix_ns_string (str): [optional]  # noqa: E501
            prefix_ns_number (float): [optional]  # noqa: E501
            prefix_ns_integer (int): [optional]  # noqa: E501
            prefix_ns_boolean (bool): [optional]  # noqa: E501
            prefix_ns_array ([int]): [optional]  # noqa: E501
            prefix_ns_wrapped_array ([int]): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in six.iteritems(kwargs):
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
