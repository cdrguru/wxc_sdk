from collections.abc import Generator

from wxc_sdk.api_child import ApiChild
from wxc_sdk.base import ApiModel, Enum
from typing import List, Optional
from pydantic import Field


__all__ = ['Action', 'AuthorizationCode', 'CLIDPolicySelection', 'CallForwardingBusyGet', 'CallForwardingNoAnswerGet', 'CallForwardingPlaceSettingGet', 'CallForwardingPlaceSettingPatch', 'CallType', 'CallingPermission', 'ExternalCallerIdNamePolicy', 'ExternalTransfer', 'Greeting', 'InterceptAnnouncementsGet', 'InterceptAnnouncementsPatch', 'InterceptIncomingGet', 'InterceptIncomingPatch', 'InterceptNumberGet', 'InterceptOutGoingGet', 'ModifyCallForwardingNoAnswer', 'MonitoredElementCallParkExtension', 'MonitoredElementItem', 'MonitoredElementUser', 'ReadCallInterceptSettingsForWorkspaceResponse', 'RetrieveAccessCodesForWorkspaceResponse', 'RetrieveCallForwardingSettingsForWorkspaceResponse', 'RetrieveCallWaitingSettingsForWorkspaceResponse', 'RetrieveCallerIDSettingsForWorkspaceResponse', 'RetrieveIncomingPermissionSettingsForWorkspaceResponse', 'RetrieveMonitoringSettingsForWorkspaceResponse', 'RetrieveOutgoingPermissionSettingsForWorkspaceResponse', 'RetrieveTransferNumbersSettingsForWorkspaceResponse', 'Type', 'Type1', 'Type2', 'UserNumberItem', 'WebexCallingWorkspaceSettingsApi']


class InterceptNumberGet(ApiModel):
    #: If true, the caller hears this new number when the call is intercepted.
    enabled: Optional[bool]
    #: New number the caller hears announced.
    destination: Optional[str]


class CallForwardingBusyGet(InterceptNumberGet):
    #: Indicates the enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
    destination_voicemail_enabled: Optional[bool]


class CallForwardingNoAnswerGet(CallForwardingBusyGet):
    #: Number of rings before the call will be forwarded if unanswered.
    number_of_rings: Optional[int]
    #: System-wide maximum number of rings allowed for numberOfRings setting.
    system_max_number_of_rings: Optional[int]


class CallForwardingPlaceSettingGet(ApiModel):
    #: Settings for forwarding all incoming calls to the destination you chose while the phone is in use or the workspace is busy.
    busy: Optional[CallForwardingBusyGet]
    #: Settings for forwarding which only occurs when you are away or not answering your phone.
    no_answer: Optional[CallForwardingNoAnswerGet]


class ModifyCallForwardingNoAnswer(CallForwardingBusyGet):
    #: Number of rings before the call will be forwarded if unanswered.
    number_of_rings: Optional[int]
    #: Max number of rings before the call will be forwarded if unanswered.
    system_max_number_of_rings: Optional[int]


class CallForwardingPlaceSettingPatch(ApiModel):
    #: Settings for forwarding all incoming calls to the destination you chose while the phone is in use or the workspace is busy.
    busy: Optional[CallForwardingBusyGet]
    #: Settings for forwarding which only occurs when you are away or not answering your phone.
    no_answer: Optional[ModifyCallForwardingNoAnswer]


class CLIDPolicySelection(ApiModel):
    #: Outgoing caller ID will show the caller's direct line number and/or extension.
    direct_line: Optional[str]
    #: Outgoing caller ID will show the main number for the location.
    location_number: Optional[str]
    #: Outgoing caller ID will show the value from the customNumber field.
    custom: Optional[str]


class ExternalCallerIdNamePolicy(str, Enum):
    #: Outgoing caller ID will show the caller's direct line name.
    direct_line = 'DIRECT_LINE'
    #: Outgoing caller ID will show the Site Name for the location.
    location = 'LOCATION'
    #: Outgoing caller ID will show the value from the customExternalCallerIdName field.
    other = 'OTHER'


class MonitoredElementCallParkExtension(ApiModel):
    #: ID of call park extension.
    id: Optional[str]
    #: Name of call park extension.
    name: Optional[str]
    #: Extension of call park extension.
    extension: Optional[str]
    #: Name of location for call park extension.
    location: Optional[str]
    #: ID of location for call park extension.
    location_id: Optional[str]


class Type(str, Enum):
    #: Object is a user.
    people = 'PEOPLE'
    #: Object is a workspace.
    place = 'PLACE'


class UserNumberItem(ApiModel):
    #: Phone number of person or workspace. Either phoneNumber or extension is mandatory.
    external: Optional[str]
    #: Extension of person or workspace. Either phoneNumber or extension is mandatory.
    extension: Optional[str]
    #: Flag to indicate primary phone.
    primary: Optional[bool]
    #: Flag to indicate toll free number.
    toll_free_number: Optional[bool]


class MonitoredElementUser(ApiModel):
    #: ID of person or workspace.
    id: Optional[str]
    #: First name of person or workspace.
    first_name: Optional[str]
    #: Last name of person or workspace.
    last_name: Optional[str]
    #: Display name of person or workspace.
    display_name: Optional[str]
    #: Type of the person or workspace.
    type: Optional[Type]
    #: Email of the person or workspace.
    email: Optional[str]
    #: List of phone numbers of the person or workspace.
    numbers: Optional[list[UserNumberItem]]
    #: Name of location for call park.
    location: Optional[str]
    #: ID of the location for call park.
    location_id: Optional[str]


class MonitoredElementItem(ApiModel):
    #: Monitored Call Park extension.
    callparkextension: Optional[MonitoredElementCallParkExtension]
    #: Monitored member for this workspace.
    member: Optional[MonitoredElementUser]


class ExternalTransfer(str, Enum):
    #: All external calls are allowed.
    allow_all_external = 'ALLOW_ALL_EXTERNAL'
    #: Only externally transferred external calls are allowed.
    allow_only_transferred_external = 'ALLOW_ONLY_TRANSFERRED_EXTERNAL'
    #: All external calls are blocked.
    block_all_external = 'BLOCK_ALL_EXTERNAL'


class CallType(str, Enum):
    #: Indicates the internal call type.
    internal_call = 'INTERNAL_CALL'
    #: Indicates the toll free call type.
    toll_free = 'TOLL_FREE'
    #: Indicates the international call type.
    international = 'INTERNATIONAL'
    #: Indicates the operator assisted call type.
    operator_assisted = 'OPERATOR_ASSISTED'
    #: Indicates the chargeable directory assisted call type.
    chargeable_directory_assisted = 'CHARGEABLE_DIRECTORY_ASSISTED'
    #: Indicates the special services I call type.
    special_services_i = 'SPECIAL_SERVICES_I'
    #: Indicates the special services II call type.
    special_services_ii = 'SPECIAL_SERVICES_II'
    #: Indicates the premium services I call type.
    premium_services_i = 'PREMIUM_SERVICES_I'
    #: Indicates the premium services II call type.
    premium_services_ii = 'PREMIUM_SERVICES_II'
    #: Indicates the national call type.
    national = 'NATIONAL'


class Action(str, Enum):
    #: The call type is allowed.
    allow = 'ALLOW'
    #: The call type is blocked.
    block = 'BLOCK'
    #: Indicates access code action for the specified call type.
    auth_code = 'AUTH_CODE'
    #: Indicates transfer number 1 for the specified call type.
    transfer_number_1 = 'TRANSFER_NUMBER_1'
    #: Indicates transfer number 2 for the specified call type.
    transfer_number_2 = 'TRANSFER_NUMBER_2'
    #: Indicates transfer number 3 for the specified call type.
    transfer_number_3 = 'TRANSFER_NUMBER_3'


class CallingPermission(ApiModel):
    #: Type of the outgoing call.
    call_type: Optional[CallType]
    #: Indicates permission for call types.
    action: Optional[Action]
    #: Indicate calling permission for call type enable status.
    transfer_enabled: Optional[bool]


class AuthorizationCode(ApiModel):
    #: Indicates an access code.
    code: Optional[str]
    #: Indicates the description of the access code.
    description: Optional[str]


class Type1(str, Enum):
    #: All incoming calls are intercepted.
    intercept_all = 'INTERCEPT_ALL'
    #: Incoming calls are not intercepted.
    allow_all = 'ALLOW_ALL'


class Greeting(str, Enum):
    #: A custom greeting is played when incoming calls are intercepted.
    custom = 'CUSTOM'
    #: A System default greeting is played when incoming calls are intercepted.
    default = 'DEFAULT'


class InterceptAnnouncementsGet(ApiModel):
    #: Indicates that a system default message will be placed when incoming calls are intercepted.
    greeting: Optional[Greeting]
    #: Filename of the custom greeting; this is an empty string if no custom greeting has been uploaded.
    filename: Optional[str]
    #: Information about the new number announcement.
    new_number: Optional[InterceptNumberGet]
    #: Information about how the call will be handled if zero (0) is pressed.
    zero_transfer: Optional[InterceptNumberGet]


class InterceptIncomingGet(ApiModel):
    #: Indicated incoming calls are intercepted.
    type: Optional[Type1]
    #: Indicates enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
    voicemail_enabled: Optional[bool]
    #: Settings related to how incoming calls are handled when the intercept feature is enabled.
    announcements: Optional[InterceptAnnouncementsGet]


class Type2(str, Enum):
    #: Outgoing calls are intercepted.
    intercept_all = 'INTERCEPT_ALL'
    #: Only non-local calls are intercepted.
    allow_local_only = 'ALLOW_LOCAL_ONLY'


class InterceptOutGoingGet(ApiModel):
    #: Indicated all outgoing calls are intercepted.
    type: Optional[Type2]
    #: If true, when the person attempts to make an outbound call, a system default message is played and the call is made to the destination phone number.
    transfer_enabled: Optional[bool]
    #: Number to which the outbound call be transferred.
    destination: Optional[str]


class InterceptAnnouncementsPatch(ApiModel):
    #: Indicates that a system default message will be placed when incoming calls are intercepted.
    greeting: Optional[Greeting]
    #: Information about the new number announcement.
    new_number: Optional[InterceptNumberGet]
    #: Information about how the call will be handled if zero (0) is pressed.
    zero_transfer: Optional[InterceptNumberGet]


class InterceptIncomingPatch(ApiModel):
    #: Indicated incoming calls are intercepted.
    type: Optional[Type1]
    #: Indicates enabled or disabled state of sending incoming calls to voicemail when the destination is an internal phone number and that number has the voicemail service enabled.
    voicemail_enabled: Optional[bool]
    #: Settings related to how incoming calls are handled when the intercept feature is enabled.
    announcements: Optional[InterceptAnnouncementsPatch]


class RetrieveCallForwardingSettingsForWorkspaceResponse(ApiModel):
    #: Call forwarding settings for a Workspace.
    call_forwarding: Optional[CallForwardingPlaceSettingGet]


class ModifyCallForwardingSettingsForWorkspaceBody(ApiModel):
    #: Call forwarding settings for a Workspace.
    call_forwarding: Optional[CallForwardingPlaceSettingPatch]


class RetrieveCallWaitingSettingsForWorkspaceResponse(ApiModel):
    #: Call Waiting state.
    enabled: Optional[bool]


class ModifyCallWaitingSettingsForWorkspaceBody(ApiModel):
    #: Call Waiting state.
    enabled: Optional[bool]


class RetrieveCallerIDSettingsForWorkspaceResponse(ApiModel):
    #: Allowed types for the selected field.
    types: Optional[list[CLIDPolicySelection]]
    #: Which type of outgoing Caller ID will be used.
    selected: Optional[CLIDPolicySelection]
    #: Direct number which will be shown if DIRECT_LINE is selected.
    direct_number: Optional[str]
    #: Location number which will be shown if LOCATION_NUMBER is selected
    location_number: Optional[str]
    #: Flag for specifying a toll-free number.
    toll_free_location_number: Optional[bool]
    #: This value must be an assigned number from the person's location.
    custom_number: Optional[str]
    #: Workspace's caller ID display name.
    display_name: Optional[str]
    #: Workspace's caller ID display details. Default is ..
    display_detail: Optional[str]
    #: Flag to block call forwarding.
    block_in_forward_calls_enabled: Optional[bool]
    #: Designates which type of External Caller ID Name policy is used. Default is DIRECT_LINE.
    external_caller_id_name_policy: Optional[ExternalCallerIdNamePolicy]
    #: Custom External Caller Name, which will be shown if External Caller ID Name is OTHER.
    custom_external_caller_id_name: Optional[str]
    #: External Caller Name, which will be shown if External Caller ID Name is OTHER.
    location_external_caller_id_name: Optional[str]


class ModifyCallerIDSettingsForWorkspaceBody(ApiModel):
    #: Which type of outgoing Caller ID will be used.
    selected: Optional[CLIDPolicySelection]
    #: This value must be an assigned number from the workspace's location.
    custom_number: Optional[str]
    #: Workspace's caller ID display name.
    display_name: Optional[str]
    #: Workspace's caller ID display details.
    display_detail: Optional[str]
    #: Flag to block call forwarding.
    block_in_forward_calls_enabled: Optional[bool]
    #: Designates which type of External Caller ID Name policy is used. Default is DIRECT_LINE.
    #: Possible values: DIRECT_LINE
    external_caller_id_name_policy: Optional[ExternalCallerIdNamePolicy]
    #: Custom External Caller Name, which will be shown if External Caller ID Name is OTHER.
    custom_external_caller_id_name: Optional[str]
    #: External Caller Name, which will be shown if External Caller ID Name is OTHER.
    location_external_caller_id_name: Optional[str]


class RetrieveMonitoringSettingsForWorkspaceResponse(ApiModel):
    #: Call park notification enabled or disabled.
    call_park_notification_enabled: Optional[bool]
    #: Monitored element items.
    monitored_elements: Optional[MonitoredElementItem]


class ModifyMonitoringSettingsForWorkspaceBody(ApiModel):
    #: Call park notification is enabled or disabled.
    enable_call_park_notification: Optional[bool]
    #: Array of ID strings of monitored elements.
    monitored_elements: Optional[list[str]]


class RetrieveIncomingPermissionSettingsForWorkspaceResponse(ApiModel):
    #: Incoming Permission state. If disabled, the default settings are used.
    use_custom_enabled: Optional[bool]
    #: Indicate call transfer setting.
    external_transfer: Optional[ExternalTransfer]
    #: Flag to indicate if workspace can receive internal calls.
    internal_calls_enabled: Optional[bool]
    #: Flag to indicate if workspace can receive collect calls.
    collect_calls_enabled: Optional[bool]


class RetrieveOutgoingPermissionSettingsForWorkspaceResponse(ApiModel):
    #: Outgoing Permission state. If disabled, the default settings are used.
    use_custom_enabled: Optional[bool]
    #: Workspace's list of outgoing permissions.
    calling_permissions: Optional[list[CallingPermission]]


class ModifyOutgoingPermissionSettingsForWorkspaceBody(ApiModel):
    #: Outgoing Permission state. If disabled, the default settings are used.
    use_custom_enabled: Optional[bool]
    #: Workspace's list of outgoing permissions.
    calling_permissions: Optional[list[CallingPermission]]


class RetrieveAccessCodesForWorkspaceResponse(ApiModel):
    #: Indicates the set of activation codes and description.
    access_codes: Optional[list[AuthorizationCode]]


class ModifyAccessCodesForWorkspaceBody(ApiModel):
    #: Indicates access codes to delete.
    delete_codes: Optional[list[str]]


class ReadCallInterceptSettingsForWorkspaceResponse(ApiModel):
    #: true if call intercept is enabled.
    enabled: Optional[bool]
    #: Settings related to how incoming calls are handled when the intercept feature is enabled.
    incoming: Optional[InterceptIncomingGet]
    #: Settings related to how outgoing calls are handled when the intercept feature is enabled.
    outgoing: Optional[InterceptOutGoingGet]


class ConfigureCallInterceptSettingsForWorkspaceBody(ApiModel):
    #: true if call interception is enabled.
    enabled: Optional[bool]
    #: Settings related to how incoming calls are handled when the intercept feature is enabled.
    incoming: Optional[InterceptIncomingPatch]
    #: Settings related to how outgoing calls are handled when the intercept feature is enabled.
    outgoing: Optional[InterceptOutGoingGet]


class RetrieveTransferNumbersSettingsForWorkspaceResponse(ApiModel):
    #: When calling a specific call type, this workspace will be automatically transferred to another number.
    auto_transfer_number1: Optional[str]
    #: When calling a specific call type, this workspace will be automatically transferred to another number.
    auto_transfer_number2: Optional[str]
    #: When calling a specific call type, this workspace will be automatically transferred to another number.
    auto_transfer_number3: Optional[str]


class WebexCallingWorkspaceSettingsApi(ApiChild, base='workspaces/{workspaceId}/features/'):
    """
    Workspaces represent places where people work, such as conference rooms, meeting spaces, lobbies, and lunchrooms. Devices may be associated with workspaces.
    Webex Calling Workspace Settings support reading and writing of Webex Calling settings for a specific workspace within the organization.
    Viewing the list of settings in a workspace requires an administrator auth token with the spark-admin:workspaces_read scope. 
    Adding, updating, or deleting settings in a workspace requires an administrator auth token with the spark-admin:workspaces_write scope.
    This API can also be used by partner administrators acting as administrators of a different organization than their own. In those cases, an orgId must be supplied, as indicated in the reference documentation for the relevant endpoints.
    A partner administrator can retrieve or change settings in a customer's organization using the optional OrgId query parameter.
    """

    def retrieve_callwarding_settings_workspace(self, workspace_id: str, org_id: str = None) -> CallForwardingPlaceSettingGet:
        """
        Retrieve Call Forwarding Settings for a Workspace.
        Two types of call forwarding are supported:
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'callForwarding')
        data = super().get(url=url, params=params)
        return data["callForwarding"]

    def modify_callwarding_settings_workspace(self, workspace_id: str, org_id: str = None, call_forwarding: CallForwardingPlaceSettingPatch):
        """
        Modify call forwarding settings for a Workspace.
        Two types of call forwarding are supported:
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param call_forwarding: Call forwarding settings for a Workspace.
        :type call_forwarding: CallForwardingPlaceSettingPatch
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if call_forwarding is not None:
            body['callForwarding'] = call_forwarding
        url = self.ep(f'callForwarding')
        super().put(url=url, params=params, json=body)
        return

    def retrieve_call_waiting_settings_workspace(self, workspace_id: str, org_id: str = None) -> bool:
        """
        Retrieve Call Waiting Settings for a Workspace.
        Call Waiting allows workspaces to handle multiple simultaneous calls. Workspaces with Call Waiting enabled can place a call on hold to answer or initiate another call.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'callWaiting')
        data = super().get(url=url, params=params)
        return data["enabled"]

    def modify_call_waiting_settings_workspace(self, workspace_id: str, org_id: str = None, enabled: bool = None):
        """
        Modify Call Waiting Settings for a Workspace.
        Call Waiting allows workspaces to handle multiple simultaneous calls. Workspaces with Call Waiting enabled can place a call on hold to answer or initiate another call.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param enabled: Call Waiting state.
        :type enabled: bool
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if enabled is not None:
            body['enabled'] = enabled
        url = self.ep(f'callWaiting')
        super().put(url=url, params=params, json=body)
        return

    def retrieve_caller_id_settings_workspace(self, workspace_id: str, org_id: str = None) -> RetrieveCallerIDSettingsForWorkspaceResponse:
        """
        Retrieve Caller ID Settings for a Workspace.
        Caller ID settings control how a workspace's information is displayed when making outgoing calls.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'callerId')
        data = super().get(url=url, params=params)
        return RetrieveCallerIDSettingsForWorkspaceResponse.parse_obj(data)

    def modify_caller_id_settings_workspace(self, workspace_id: str, org_id: str = None, selected: enum, custom_number: str = None, display_name: str = None, display_detail: str = None, block_in_forward_calls_enabled: bool = None, external_caller_id_name_policy: ExternalCallerIdNamePolicy = None, custom_external_caller_id_name: str = None, location_external_caller_id_name: str = None):
        """
        Modify Caller ID settings for a Workspace.
        Caller ID settings control how a workspace's information is displayed when making outgoing calls.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param selected: Which type of outgoing Caller ID will be used.
        :type selected: enum
        :param custom_number: This value must be an assigned number from the workspace's location.
        :type custom_number: str
        :param display_name: Workspace's caller ID display name.
        :type display_name: str
        :param display_detail: Workspace's caller ID display details.
        :type display_detail: str
        :param block_in_forward_calls_enabled: Flag to block call forwarding.
        :type block_in_forward_calls_enabled: bool
        :param external_caller_id_name_policy: Designates which type of External Caller ID Name policy is used. Default is DIRECT_LINE.
Possible values: DIRECT_LINE
        :type external_caller_id_name_policy: ExternalCallerIdNamePolicy
        :param custom_external_caller_id_name: Custom External Caller Name, which will be shown if External Caller ID Name is OTHER.
        :type custom_external_caller_id_name: str
        :param location_external_caller_id_name: External Caller Name, which will be shown if External Caller ID Name is OTHER.
        :type location_external_caller_id_name: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if selected is not None:
            body['selected'] = selected
        if custom_number is not None:
            body['customNumber'] = custom_number
        if display_name is not None:
            body['displayName'] = display_name
        if display_detail is not None:
            body['displayDetail'] = display_detail
        if block_in_forward_calls_enabled is not None:
            body['blockInForwardCallsEnabled'] = block_in_forward_calls_enabled
        if external_caller_id_name_policy is not None:
            body['externalCallerIdNamePolicy'] = external_caller_id_name_policy
        if custom_external_caller_id_name is not None:
            body['customExternalCallerIdName'] = custom_external_caller_id_name
        if location_external_caller_id_name is not None:
            body['locationExternalCallerIdName'] = location_external_caller_id_name
        url = self.ep(f'callerId')
        super().put(url=url, params=params, json=body)
        return

    def retrieve_monitoring_settings_workspace(self, workspace_id: str, org_id: str = None) -> RetrieveMonitoringSettingsForWorkspaceResponse:
        """
        Retrieves Monitoring settings for a Workspace.
        Allow workspaces to monitor the line status of specified agents, workspaces, or call park extensions. The line status indicates if a monitored agent or a workspace is on a call, or if a call has been parked on the monitored call park extension.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'monitoring')
        data = super().get(url=url, params=params)
        return RetrieveMonitoringSettingsForWorkspaceResponse.parse_obj(data)

    def modify_monitoring_settings_workspace(self, workspace_id: str, org_id: str = None, enable_call_park_notification: bool = None, monitored_elements: List[str] = None):
        """
        Modify Monitoring settings for a Workspace.
        Allow workspaces to monitor the line status of specified agents, workspaces, or call park extensions. The line status indicates if a monitored agent or a workspace is on a call, or if a call has been parked on the monitored call park extension.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param enable_call_park_notification: Call park notification is enabled or disabled.
        :type enable_call_park_notification: bool
        :param monitored_elements: Array of ID strings of monitored elements.
        :type monitored_elements: List[str]
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if enable_call_park_notification is not None:
            body['enableCallParkNotification'] = enable_call_park_notification
        if monitored_elements is not None:
            body['monitoredElements'] = monitored_elements
        url = self.ep(f'monitoring')
        super().put(url=url, params=params, json=body)
        return

    def retrieve_incoming_permission_settings_workspace(self, workspace_id: str, org_id: str = None) -> RetrieveIncomingPermissionSettingsForWorkspaceResponse:
        """
        Retrieve Incoming Permission settings for a Workspace.
        Incoming permission settings allow modifying permissions for a workspace that can be different from the organization's default to manage different call types.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'incomingPermission')
        data = super().get(url=url, params=params)
        return RetrieveIncomingPermissionSettingsForWorkspaceResponse.parse_obj(data)

    def modify_incoming_permission_settings_workspace(self, workspace_id: str, org_id: str = None, use_custom_enabled: bool = None, external_transfer: enum = None, internal_calls_enabled: bool = None, collect_calls_enabled: bool = None):
        """
        Modify Incoming Permission settings for a Workspace.
        Incoming permission settings allow modifying permissions for a workspace that can be different from the organization's default to manage different call types.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param use_custom_enabled: Incoming Permission state. If disabled, the default settings are used.
        :type use_custom_enabled: bool
        :param external_transfer: Indicate call transfer setting.
        :type external_transfer: enum
        :param internal_calls_enabled: Flag to indicate if the workspace can receive internal calls.
        :type internal_calls_enabled: bool
        :param collect_calls_enabled: Flag to indicate if the workspace can receive collect calls.
        :type collect_calls_enabled: bool
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if use_custom_enabled is not None:
            body['useCustomEnabled'] = use_custom_enabled
        if external_transfer is not None:
            body['externalTransfer'] = external_transfer
        if internal_calls_enabled is not None:
            body['internalCallsEnabled'] = internal_calls_enabled
        if collect_calls_enabled is not None:
            body['collectCallsEnabled'] = collect_calls_enabled
        url = self.ep(f'incomingPermission')
        super().put(url=url, params=params, json=body)
        return

    def retrieve_outgoing_permission_settings_workspace(self, workspace_id: str, org_id: str = None) -> RetrieveOutgoingPermissionSettingsForWorkspaceResponse:
        """
        Retrieve Outgoing Permission settings for a Workspace.
        Turn on outgoing call settings for this workspace to override the calling settings from the location that are used by default.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'outgoingPermission')
        data = super().get(url=url, params=params)
        return RetrieveOutgoingPermissionSettingsForWorkspaceResponse.parse_obj(data)

    def modify_outgoing_permission_settings_workspace(self, workspace_id: str, org_id: str = None, use_custom_enabled: bool = None, calling_permissions: List[CallingPermission] = None):
        """
        Modify Outgoing Permission settings for a Place.
        Turn on outgoing call settings for this workspace to override the calling settings from the location that are used by default.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param use_custom_enabled: Outgoing Permission state. If disabled, the default settings are used.
        :type use_custom_enabled: bool
        :param calling_permissions: Workspace's list of outgoing permissions.
        :type calling_permissions: List[CallingPermission]
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if use_custom_enabled is not None:
            body['useCustomEnabled'] = use_custom_enabled
        if calling_permissions is not None:
            body['callingPermissions'] = calling_permissions
        url = self.ep(f'outgoingPermission')
        super().put(url=url, params=params, json=body)
        return

    def retrieve_access_codes_workspace(self, workspace_id: str, org_id: str = None) -> List[AuthorizationCode]:
        """
        Retrieve Access codes for a Workspace.
        Access codes are used to bypass permissions.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'outgoingPermission/accessCodes')
        data = super().get(url=url, params=params)
        return data["accessCodes"]

    def modify_access_codes_workspace(self, workspace_id: str, org_id: str = None, delete_codes: List[str] = None):
        """
        Modify Access codes for a workspace.
        Access codes are used to bypass permissions.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param delete_codes: Indicates access codes to delete.
        :type delete_codes: List[str]
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if delete_codes is not None:
            body['deleteCodes'] = delete_codes
        url = self.ep(f'outgoingPermission/accessCodes')
        super().put(url=url, params=params, json=body)
        return

    def create_access_codes_workspace(self, workspace_id: str, org_id: str = None, code: str, description: str):
        """
        Create new Access codes for the given workspace.
        Access codes are used to bypass permissions.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param code: Indicates an access code.
        :type code: str
        :param description: Indicates the description of the access code.
        :type description: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if code is not None:
            body['code'] = code
        if description is not None:
            body['description'] = description
        url = self.ep(f'outgoingPermission/accessCodes')
        super().post(url=url, params=params, json=body)
        return

    def read_call_intercept_settings_workspace(self, workspace_id: str, org_id: str = None) -> ReadCallInterceptSettingsForWorkspaceResponse:
        """
        Retrieves Workspace's Call Intercept Settings
        The intercept feature gracefully takes a workspace's phone out of service, while providing callers with informative announcements and alternative routing options. Depending on the service configuration, none, some, or all incoming calls to the specified workspace are intercepted. Also depending on the service configuration, outgoing calls are intercepted or rerouted to another location.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'intercept')
        data = super().get(url=url, params=params)
        return ReadCallInterceptSettingsForWorkspaceResponse.parse_obj(data)

    def configure_call_intercept_settings_workspace(self, workspace_id: str, org_id: str = None, enabled: bool = None, incoming: InterceptIncomingPatch = None, outgoing: InterceptOutGoingGet = None):
        """
        Configures a Workspace's Call Intercept Settings
        The intercept feature gracefully takes a workspace's phone out of service, while providing callers with informative announcements and alternative routing options. Depending on the service configuration, none, some, or all incoming calls to the specified person are intercepted. Also depending on the service configuration, outgoing calls are intercepted or rerouted to another location.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_write or a user auth token with spark:workspaces_read scope can be used by a person to read their settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param enabled: true if call interception is enabled.
        :type enabled: bool
        :param incoming: Settings related to how incoming calls are handled when the intercept feature is enabled.
        :type incoming: InterceptIncomingPatch
        :param outgoing: Settings related to how outgoing calls are handled when the intercept feature is enabled.
        :type outgoing: InterceptOutGoingGet
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if enabled is not None:
            body['enabled'] = enabled
        if incoming is not None:
            body['incoming'] = incoming
        if outgoing is not None:
            body['outgoing'] = outgoing
        url = self.ep(f'intercept')
        super().put(url=url, params=params, json=body)
        return

    def retrieve_transfer_numbers_settings_workspace(self, workspace_id: str, org_id: str = None) -> RetrieveTransferNumbersSettingsForWorkspaceResponse:
        """
        Retrieve Transfer Numbers Settings for a Workspace.
        When calling a specific call type, this workspace will be automatically transferred to another number. The person assigned the Auto Transfer Number can then approve the call and send it through or reject the call type. You can add up to 3 numbers.
        This API requires a full or read-only administrator auth token with a scope of spark-admin:workspaces_read or a user auth token with spark:workspaces_read scope can be used to read workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        url = self.ep(f'outgoingPermission/autoTransferNumbers')
        data = super().get(url=url, params=params)
        return RetrieveTransferNumbersSettingsForWorkspaceResponse.parse_obj(data)

    def modify_transfer_numbers_settings_workspace(self, workspace_id: str, org_id: str = None, auto_transfer_number1: str = None, auto_transfer_number2: str = None, auto_transfer_number3: str = None):
        """
        Modify Transfer Numbers Settings for a place.
        When calling a specific call type, this workspace will be automatically transferred to another number. The person assigned the Auto Transfer Number can then approve the call and send it through or reject the call type. You can add up to 3 numbers.
        This API requires a full or user administrator auth token with the spark-admin:workspaces_write scope or a user auth token with spark:workspaces_write scope can be used to update workspace settings.

        :param workspace_id: Unique identifier for the workspace.
        :type workspace_id: str
        :param org_id: ID of the organization within which the workspace resides. Only admin users of another organization (such as partners) may use this parameter as the default is the same organization as the token used to access API.
        :type org_id: str
        :param auto_transfer_number1: When calling a specific call type, this workspace will be automatically transferred to another number.
        :type auto_transfer_number1: str
        :param auto_transfer_number2: When calling a specific call type, this workspace will be automatically transferred to another number.
        :type auto_transfer_number2: str
        :param auto_transfer_number3: When calling a specific call type, this workspace will be automatically transferred to another number.
        :type auto_transfer_number3: str
        """
        params = {}
        if org_id is not None:
            params['orgId'] = org_id
        body = {}
        if auto_transfer_number1 is not None:
            body['autoTransferNumber1'] = auto_transfer_number1
        if auto_transfer_number2 is not None:
            body['autoTransferNumber2'] = auto_transfer_number2
        if auto_transfer_number3 is not None:
            body['autoTransferNumber3'] = auto_transfer_number3
        url = self.ep(f'outgoingPermission/autoTransferNumbers')
        super().put(url=url, params=params, json=body)
        return
