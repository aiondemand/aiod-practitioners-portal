# ExperimentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**experiment_template_id** | **str** |  | 
**publication_ids** | **List[str]** |  | [optional] [default to []]
**dataset_ids** | **List[str]** |  | 
**model_ids** | **List[str]** |  | 
**env_vars** | [**List[EnvironmentVar]**](EnvironmentVar.md) |  | 
**public** | **bool** |  | 
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**archived** | **bool** |  | 
**mine** | **bool** |  | 

## Example

```python
from aiod_rail_sdk.models.experiment_response import ExperimentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExperimentResponse from a JSON string
experiment_response_instance = ExperimentResponse.from_json(json)
# print the JSON string representation of the object
print(ExperimentResponse.to_json())

# convert the object into a dict
experiment_response_dict = experiment_response_instance.to_dict()
# create an instance of ExperimentResponse from a dict
experiment_response_from_dict = ExperimentResponse.from_dict(experiment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

