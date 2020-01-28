# coding: utf-8

"""
    Kibernetika project, backend component

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from kclient.api_client import ApiClient


class ServingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def serving_delete(self, workspace, serving, **kwargs):  # noqa: E501
        """Delete serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_delete(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :param bool dependencies: Get only dependencies
        :param str confirm: String for confirmation
        :param bool force: Force deletion
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.serving_delete_with_http_info(workspace, serving, **kwargs)  # noqa: E501
        else:
            (data) = self.serving_delete_with_http_info(workspace, serving, **kwargs)  # noqa: E501
            return data

    def serving_delete_with_http_info(self, workspace, serving, **kwargs):  # noqa: E501
        """Delete serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_delete_with_http_info(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :param bool dependencies: Get only dependencies
        :param str confirm: String for confirmation
        :param bool force: Force deletion
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace', 'serving', 'dependencies', 'confirm', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serving_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `serving_delete`")  # noqa: E501
        # verify the required parameter 'serving' is set
        if ('serving' not in params or
                params['serving'] is None):
            raise ValueError("Missing the required parameter `serving` when calling `serving_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501
        if 'serving' in params:
            path_params['serving'] = params['serving']  # noqa: E501

        query_params = []
        if 'dependencies' in params:
            query_params.append(('dependencies', params['dependencies']))  # noqa: E501
        if 'confirm' in params:
            query_params.append(('confirm', params['confirm']))  # noqa: E501
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.2/workspace/{workspace}/serving/{serving}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def serving_disable(self, workspace, serving, **kwargs):  # noqa: E501
        """Disable serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_disable(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.serving_disable_with_http_info(workspace, serving, **kwargs)  # noqa: E501
        else:
            (data) = self.serving_disable_with_http_info(workspace, serving, **kwargs)  # noqa: E501
            return data

    def serving_disable_with_http_info(self, workspace, serving, **kwargs):  # noqa: E501
        """Disable serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_disable_with_http_info(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace', 'serving']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serving_disable" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `serving_disable`")  # noqa: E501
        # verify the required parameter 'serving' is set
        if ('serving' not in params or
                params['serving'] is None):
            raise ValueError("Missing the required parameter `serving` when calling `serving_disable`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501
        if 'serving' in params:
            path_params['serving'] = params['serving']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.2/workspace/{workspace}/serving/{serving}/disable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelsServing',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def serving_enable(self, workspace, serving, **kwargs):  # noqa: E501
        """Enable serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_enable(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.serving_enable_with_http_info(workspace, serving, **kwargs)  # noqa: E501
        else:
            (data) = self.serving_enable_with_http_info(workspace, serving, **kwargs)  # noqa: E501
            return data

    def serving_enable_with_http_info(self, workspace, serving, **kwargs):  # noqa: E501
        """Enable serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_enable_with_http_info(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace', 'serving']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serving_enable" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `serving_enable`")  # noqa: E501
        # verify the required parameter 'serving' is set
        if ('serving' not in params or
                params['serving'] is None):
            raise ValueError("Missing the required parameter `serving` when calling `serving_enable`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501
        if 'serving' in params:
            path_params['serving'] = params['serving']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.2/workspace/{workspace}/serving/{serving}/enable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelsServing',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def serving_info(self, workspace, serving, **kwargs):  # noqa: E501
        """Return serving's info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_info(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.serving_info_with_http_info(workspace, serving, **kwargs)  # noqa: E501
        else:
            (data) = self.serving_info_with_http_info(workspace, serving, **kwargs)  # noqa: E501
            return data

    def serving_info_with_http_info(self, workspace, serving, **kwargs):  # noqa: E501
        """Return serving's info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_info_with_http_info(workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace', 'serving']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serving_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `serving_info`")  # noqa: E501
        # verify the required parameter 'serving' is set
        if ('serving' not in params or
                params['serving'] is None):
            raise ValueError("Missing the required parameter `serving` when calling `serving_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501
        if 'serving' in params:
            path_params['serving'] = params['serving']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.2/workspace/{workspace}/serving/{serving}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelsServing',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def serving_project_job(self, job, workspace, serving, **kwargs):  # noqa: E501
        """Serving result jobs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_project_job(job, workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job: Serving job ID (required)
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ApplicationProjectServingJob
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.serving_project_job_with_http_info(job, workspace, serving, **kwargs)  # noqa: E501
        else:
            (data) = self.serving_project_job_with_http_info(job, workspace, serving, **kwargs)  # noqa: E501
            return data

    def serving_project_job_with_http_info(self, job, workspace, serving, **kwargs):  # noqa: E501
        """Serving result jobs  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_project_job_with_http_info(job, workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job: Serving job ID (required)
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ApplicationProjectServingJob
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job', 'workspace', 'serving']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serving_project_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job' is set
        if ('job' not in params or
                params['job'] is None):
            raise ValueError("Missing the required parameter `job` when calling `serving_project_job`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `serving_project_job`")  # noqa: E501
        # verify the required parameter 'serving' is set
        if ('serving' not in params or
                params['serving'] is None):
            raise ValueError("Missing the required parameter `serving` when calling `serving_project_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'job' in params:
            path_params['job'] = params['job']  # noqa: E501
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501
        if 'serving' in params:
            path_params['serving'] = params['serving']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.2/workspace/{workspace}/serving/{serving}/projresult/job/{job}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApplicationProjectServingJob',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def serving_proxy(self, body, workspace, serving, **kwargs):  # noqa: E501
        """Proxy to serving (json data)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_proxy(body, workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsArbitrary body: (required)
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsArbitrary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.serving_proxy_with_http_info(body, workspace, serving, **kwargs)  # noqa: E501
        else:
            (data) = self.serving_proxy_with_http_info(body, workspace, serving, **kwargs)  # noqa: E501
            return data

    def serving_proxy_with_http_info(self, body, workspace, serving, **kwargs):  # noqa: E501
        """Proxy to serving (json data)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.serving_proxy_with_http_info(body, workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ModelsArbitrary body: (required)
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsArbitrary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'workspace', 'serving']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method serving_proxy" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `serving_proxy`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `serving_proxy`")  # noqa: E501
        # verify the required parameter 'serving' is set
        if ('serving' not in params or
                params['serving'] is None):
            raise ValueError("Missing the required parameter `serving` when calling `serving_proxy`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501
        if 'serving' in params:
            path_params['serving'] = params['serving']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.2/workspace/{workspace}/serving/{serving}/proxy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelsArbitrary',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_serving(self, body, workspace, serving, **kwargs):  # noqa: E501
        """Update serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_serving(body, workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MlappServing body: (required)
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_serving_with_http_info(body, workspace, serving, **kwargs)  # noqa: E501
        else:
            (data) = self.update_serving_with_http_info(body, workspace, serving, **kwargs)  # noqa: E501
            return data

    def update_serving_with_http_info(self, body, workspace, serving, **kwargs):  # noqa: E501
        """Update serving  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_serving_with_http_info(body, workspace, serving, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MlappServing body: (required)
        :param str workspace: Workspace's name (required)
        :param str serving: Serving's Name or ID (required)
        :return: ModelsServing
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'workspace', 'serving']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_serving" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_serving`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `update_serving`")  # noqa: E501
        # verify the required parameter 'serving' is set
        if ('serving' not in params or
                params['serving'] is None):
            raise ValueError("Missing the required parameter `serving` when calling `update_serving`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501
        if 'serving' in params:
            path_params['serving'] = params['serving']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/v0.2/workspace/{workspace}/serving/{serving}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModelsServing',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
