import json
import aiod_rail_sdk
from typing import Union


class ExperimentsTemplates:
    def __init__(self, 
                 client_config: aiod_rail_sdk.Configuration):
        self._configuration = client_config
            
    def create_experiment_template(
            self, 
            file: Union[dict, tuple[str, str, str, dict]]
            ) -> aiod_rail_sdk.ExperimentTemplateResponse:
        """
            Creates experiment template for experiment.
            Args:
                file: (Union[dict, tuple[str, str, str, dict]]): The file can be passed either as full specified json (dictionary)
                                                                 or as a tuple of three strings and a json (dictionary) specifying 
                                                                 the paths to script, requirements and docker image in this order 
                                                                 and template description (name, description, task etc.).
            Returns:
                aiod_rail_sdk.ExperimentTemplateResponse: Created experiment template.
        """
        json_data = None
        if isinstance(file, dict):
            json_data = json.dumps(file)
        
        elif isinstance(file, tuple) and len(file) == 4 and all(isinstance(item, (str, dict)) for item in file):
            path_script, path_requirements, path_image, config = file
            if isinstance(config, dict):
                with open(path_script, 'r') as s, open(path_requirements, 'r') as r, open(path_image, 'r') as i:
                    script = s.read()
                    requirements = r.read()
                    image = i.read()
                    config.update({'script': script, 'pip_requirements': requirements, 'base_image': image})
                    json_data = json.dumps(config)
            else:
                raise ValueError("Fourth element must be a dictionary")
        else:
            raise ValueError("Invalid input format")
        
        experiment_template_create_instance = aiod_rail_sdk.ExperimentTemplateCreate.from_json(json_data)

        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)
            experiment_template_create = experiment_template_create_instance

            try:
                api_response = api_instance.create_experiment_template_v1_experiment_templates_post(experiment_template_create)
                return api_response
            
            except Exception as e:
                raise(f'Exception {e}')
            
            
    def approve_experiment_template(self, 
                                    id: str, 
                                    password: str = 'pass', 
                                    is_approved: bool = False) -> None:
        """
            Approves experiment template with specified ID.
            Args:
                id (str): ID of experiment template to be approved.
                password (str): Password required to be able to approve the experiment template.
                approve_value (bool, optional): Boolean value to approve/reject the experiment template. Defaults to False.
            
            Returns:
                None.
        """
        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)

            try:
                api_response = api_instance.approve_experiment_template_v1_experiment_templates_id_approve_patch(id, password, approved=is_approved)
                return api_response
            except Exception as e:
                raise(f'Exception {e}')

    def count(self, 
              query: str = '', 
              mine: bool = True, 
              finalized: bool = True, 
              approved: bool = True, 
              public: bool = True) -> int:
        """
            Gets experiment templates count.
            Args:
                query (str, optional): Query used to filter experiment templates. Defaults to empty string, which means that by default count is not filtered.
                mine (bool, optional): If own personal experiment templates should be counted. Defaults to True.
                finalized (bool, optional): If experiment templates that are succesfully build and ready to use should be counted as well. Defaults to True.
                approved (bool, optional): If already approved experiments should be counted as well. Defaults to True.
                public (bool, optional): If experiment templates flagged as public should be counted as well. Defaults to True.

            Returns:
                int: Number of experiment templates.
        """
        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)
            
            try:
                api_response = api_instance.get_experiment_templates_count_v1_count_experiment_templates_get(
                    query=query,
                    mine=mine, 
                    approved=approved,
                    public=public,
                    finalized=finalized,
                )
                return api_response
            except Exception as e:
                raise(f'Exception {e}')

    def get(self,
            query: str = '', 
            mine: bool = True, 
            finalized: bool = True,
            approved: bool = True,
            public: bool = True, 
            offset: int = 0, 
            limit: int = 100) -> list[aiod_rail_sdk.ExperimentTemplateResponse]:
        """
            Gets experiment templates in specified range.
            Args:
                query (str, optional): Query used to filter experiment templates. Defaults to empty string, which means that by default, it's not used.
                mine (bool, optional): If own personal experiment templates should be included. Defaults to True.
                finalized (bool, optional): If experiment templates that are succesfully build and ready to use should be listed as well. Defaults to True.
                approved (bool, optional): If already approved experiments should be listed as well. Defaults to True.
                public (bool, optional): If experiment templates flagged as public should be listed as well. Defaults to True.
                offset (int, optional): Starting index of experiment template range from which to retrieve Defaults to 0.
                limit (int, optional): Ending index of experiment template range to which to retrieve. Defaults to 100.

            Returns:
                list[aiod_rail_sdk.ExperimentTemplateResponse]: List of all experiments in given range
        """
        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)
            
            try:
                api_response = api_instance.get_experiment_templates_v1_experiment_templates_get(
                    query=query,
                    mine=mine, 
                    approved=approved,
                    public=public,
                    finalized=finalized, 
                    offset=offset, 
                    limit=limit
                )
                return api_response
            except Exception as e:
                raise(f'Exception {e}')

    def get_by_id(self, 
                  id: str) -> aiod_rail_sdk.ExperimentTemplateResponse:
        """
            Gets specific experiment template by it's ID.
            Args:
                id (str): ID of experiment template to be retrieved.
            Returns:
                aiod_rail_sdk.ExperimentTemplateResponse: Experiment template given by ID.
        """
        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)
            
            try:
                api_response = api_instance.get_experiment_template_v1_experiment_templates_id_get(id)
                return api_response
            except Exception as e:
                raise(f'Exception {e}')
            

    def remove(self,
               id: str) -> None:
        """
            Remove specific experiment template specified by ID.
            Args:
                id (str): ID of experiment template to be removed.
            Returns:
                None.
        """
        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)
            
            try:
                api_instance.remove_experiment_template_v1_experiment_templates_id_delete(id)
            except Exception as e:
                raise(f'Exception {e}')

    def archive(self,
                id: str,
                archived: bool = False) -> None:
        """
            Archives specific experiment template specified by ID.
            Args:
                id (str): ID of experiment template to be archived.
                archived (bool): If experiment template should be archived or un-archived. Defaults to False.
            Returns:
                None.
        """
        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)
            
            try:
                api_instance.archive_experiment_template_v1_experiment_templates_id_archive_patch(id=id, archived=archived)
            except Exception as e:
                raise(f'Exception {e}')

    def update(self,
               id: str,
               file: dict) -> aiod_rail_sdk.ExperimentTemplateResponse:
        """
            Updates specific experiment template.
            Args:
                id (str): ID of experiment template to be updated.
                file: (Union[dict, tuple[str, str, str, dict]]): The file can be passed either as full specified json (dictionary)
                                                                 or as a tuple of three strings and a json (dictionary) specifying 
                                                                 the paths to script, requirements and docker image in this order 
                                                                 and template description (name, description, task etc.).
            Returns:
                aiod_rail_sdk.ExperimentTemplateResponse: Updated Experiment template by given ID.
        """
        json_data = None
        if isinstance(file, dict):
            json_data = json.dumps(file)
        
        elif isinstance(file, tuple) and len(file) == 4 and all(isinstance(item, (str, dict)) for item in file):
            path_script, path_requirements, path_image, config = file
            if isinstance(config, dict):
                with open(path_script, 'r') as s, open(path_requirements, 'r') as r, open(path_image, 'r') as i:
                    script = s.read()
                    requirements = r.read()
                    image = i.read()
                    config.update({'script': script, 'pip_requirements': requirements, 'base_image': image})
                    json_data = json.dumps(config)
            else:
                raise ValueError("Fourth element must be a dictionary")
        else:
            raise ValueError("Invalid input format")
        
        experiment_template_create_instance = aiod_rail_sdk.ExperimentTemplateCreate.from_json(json_data)

        with aiod_rail_sdk.ApiClient(self._configuration) as api_client:
            api_instance = aiod_rail_sdk.ExperimentTemplatesApi(api_client)
            
            try:
                api_response = api_instance.update_experiment_template_v1_experiment_templates_id_put(id, experiment_template_create=experiment_template_create_instance)
                return api_response
            except Exception as e:
                raise(f'Exception {e}')

    