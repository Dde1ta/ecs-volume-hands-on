import json
import os
from typing import List, Tuple, Type, Union

from models import Student, Course, Teacher

# Helper alias for readability
ModelType = Union[Student, Teacher, Course]


class Data:

    def __init__(self):
        self.data_location = os.getenv("DATA_LOCATION", None)

        if self.data_location is None:
            raise Exception("Data Location Not Set :(")

        self.__init_files__()

    def __init_files__(self):
        if not os.path.exists(self.data_location):
            os.mkdir(self.data_location)

        if not os.path.exists(os.path.join(self.data_location, f"student.json")):
            file = open(os.path.join(self.data_location, f"student.json"), 'w')
            file.close()

        if not os.path.exists(os.path.join(self.data_location, f"course.json")):
            file = open(os.path.join(self.data_location, f"course.json"), 'w')
            file.close()

        if not os.path.exists(os.path.join(self.data_location, f"teacher.json")):
            file = open(os.path.join(self.data_location, f"teacher.json"), 'w')
            file.close()

    def get_all(self, model: Type[ModelType]) -> Tuple[ModelType, ...]:
        data = []
        file_path = os.path.join(self.data_location, f"{model.entity}.json")

        with open(file_path, "r") as file:
            json_data = json.load(file)

        for data_item in json_data:
            data.append(model.model_construct(
                **data_item
            ))

        return tuple(data)

    def get_id(self, model: Type[ModelType], _id: int) -> ModelType:
        file_path = os.path.join(self.data_location, f"{model.entity}.json")

        with open(file_path, "r") as file:
            json_data = json.load(file)

        for data_item in json_data:
            if data_item.get("id") == _id:
                return model.model_construct(**data_item)

        # FIX: Raise ValueError instead of FileNotFoundError
        raise ValueError(f"id not found for {model.entity}")

    def update_id(self, new_obj: ModelType, _id: int) -> bool:
        file_path = os.path.join(self.data_location, f"{new_obj.entity}.json")

        with open(file_path, "r") as file:
            json_data = json.load(file)

        updated = False
        for i, data_item in enumerate(json_data):
            if data_item.get("id") == _id:
                json_data[i] = new_obj.model_dump()
                updated = True
                break

        if updated:
            with open(file_path, "w") as file:
                json.dump(json_data, file, indent=4)
            return True

        return False

    def add(self, new_obj: ModelType) -> bool:
        file_path = os.path.join(self.data_location, f"{new_obj.entity}.json")

        # Load existing array of objects, or start a new one if file doesn't exist
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    json_data = json.load(file)
                except json.JSONDecodeError:
                    # Handle empty or corrupted file
                    json_data = []
        else:
            json_data = []

        # Prevent duplicate IDs
        for data_item in json_data:
            if data_item.get("id") == new_obj.id:
                raise ValueError(f"An entry with id {new_obj.id} already exists in {new_obj.entity}.json")

        # Append new object as a dictionary to the array
        json_data.append(new_obj.model_dump())

        # Write the updated array back to the JSON file
        with open(file_path, "w") as file:
            json.dump(json_data, file, indent=4)

        return True
