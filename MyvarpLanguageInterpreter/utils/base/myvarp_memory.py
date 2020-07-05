from utils.base.processors.operation import Identifier
from utils.builtins.constants import BUILTINS


class MyvarpMemory:
    def __init__(self):
        self.__builtins = BUILTINS
        self.__memory = {}

    class Reference:

        def __init__(self, memory, name):
            self._parent_referenced = None
            self._memory = memory
            self._name = name

        class MemoryItem:
            def __init__(self, data: dict):
                self._key = data['key']
                self._value = data['value']

            def get_key(self):
                return self._key

            def get_value(self):
                return self._value

            def __str__(self):
                return self.__repr__()

            def __repr__(self):
                return f'MemoryItem<{self.get_key()}: {self.get_value()}>'

        def get_referenced_value(self):
            return self.MemoryItem(self._memory.get_item(self._name)['value'])

        def get_referenced_key(self):
            return self._name

        def get_referenced_parent_key(self):
            return self.get_referenced_value().get_key()

        def __str__(self):
            return self.__repr__()

        def __repr__(self):
            return f'MemoryReference<{self.get_referenced_key()}: {self.get_referenced_value()}>'

    def set_item(self, key, value, **kwargs):

        if kwargs.keys().__contains__('assign_type'):

            assign_type = kwargs['assign_type']

            if assign_type == 'new':
                # detach from reference parent and set n
                self.__memory[f'{key}'] = self.get_data_for(value) if isinstance(value, str) else value
            else:
                if self.has_key(key) and isinstance(self.get_value_for(key), self.Reference):
                    key = self.get_value_for(key).get_referenced_key()
                # print(f'doing assignment: {key} = {assign_type} {value}')
                if assign_type == 'val':
                    self.__memory[f'{key}'] = self.get_data_for(value) if isinstance(value, str) else value
                elif assign_type == 'ref':
                    temp_value = self.get_value_for(value)
                    if isinstance(temp_value, self.Reference):
                        self.get_referenced_value_for(value)
                        if temp_value.get_referenced_parent_key() != key:
                            self.__memory[f'{key}'] = self.reference(value)
                    else:
                        self.__memory[f'{key}'] = self.reference(value)

        else:
            if self.has_key(key) and isinstance(self.get_value_for(key), self.Reference):
                key = self.get_value_for(key).get_referenced_key()
            self.__memory[f'{key}'] = value

    def get_all_items(self):
        return dict(self.__memory)

    def get_item(self, key):
        if self.has_key(key):
            value = self.get_referenced_value_for(key)
            if isinstance(value, self.Reference):
                return self.get_referenced_value_for(value.get_referenced_key())
            else:
                return {'key': key, 'value': value}

    def get_referenced_value_for(self, key):
        # print(f'getting referenced value for: {key}')
        if self.has_key(key):
            value = self.get_value_for(key)
            # print(f'value: {value} is reference: {isinstance(value, self.Reference)}')
            if isinstance(value, self.Reference):
                # print(f'try again referenced value for: {value.get_referenced_key()}')
                return self.get_referenced_value_for(value.get_referenced_key())
            else:
                return {'key': key, 'value': value}

    def get_value_for(self, key):
        if self.has_key(key):
            return self.__memory[f'{key}']

    def get_data_for(self, key):
        if self.has_key(key):
            return self.get_referenced_value_for(key)['value']

    def get_keys(self):
        return list(self.__memory.keys())

    def get_values(self):
        return list(self.__memory.values())

    def has_key(self, item):
        return self.get_keys().__contains__(item)

    def has_value(self, item):
        return self.get_values().__contains__(item)

    def contains(self, key, value):
        if key in self.get_keys():
            return self.get_referenced_value_for(value) == value

    def reference(self, name):
        return self.Reference(self, name)

    def get_mem_location_id(self, name):
        if self.has_key(name):
            return id(self.get_data_for(name))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'MyvarpMemory<{self.__memory}>'

    def __contains__(self, item):
        self.has_key(item)
