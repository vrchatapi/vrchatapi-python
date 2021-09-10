# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from vrchatapi.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from vrchatapi.model.avatar import Avatar
from vrchatapi.model.avatar_id import AvatarID
from vrchatapi.model.avatar_unity_package_url_object import AvatarUnityPackageUrlObject
from vrchatapi.model.config import Config
from vrchatapi.model.config_announcements import ConfigAnnouncements
from vrchatapi.model.config_download_urls import ConfigDownloadUrls
from vrchatapi.model.config_dynamic_world_rows import ConfigDynamicWorldRows
from vrchatapi.model.config_events import ConfigEvents
from vrchatapi.model.current_user import CurrentUser
from vrchatapi.model.deployment_group import DeploymentGroup
from vrchatapi.model.developer_type import DeveloperType
from vrchatapi.model.error import Error
from vrchatapi.model.favorite import Favorite
from vrchatapi.model.favorite_group import FavoriteGroup
from vrchatapi.model.favorite_group_id import FavoriteGroupID
from vrchatapi.model.favorite_group_visibility import FavoriteGroupVisibility
from vrchatapi.model.favorite_id import FavoriteID
from vrchatapi.model.favorite_type import FavoriteType
from vrchatapi.model.file import File
from vrchatapi.model.file_data import FileData
from vrchatapi.model.file_id import FileID
from vrchatapi.model.file_status import FileStatus
from vrchatapi.model.file_version import FileVersion
from vrchatapi.model.friend_status import FriendStatus
from vrchatapi.model.inline_object import InlineObject
from vrchatapi.model.inline_object1 import InlineObject1
from vrchatapi.model.inline_object10 import InlineObject10
from vrchatapi.model.inline_object11 import InlineObject11
from vrchatapi.model.inline_object12 import InlineObject12
from vrchatapi.model.inline_object13 import InlineObject13
from vrchatapi.model.inline_object2 import InlineObject2
from vrchatapi.model.inline_object3 import InlineObject3
from vrchatapi.model.inline_object4 import InlineObject4
from vrchatapi.model.inline_object5 import InlineObject5
from vrchatapi.model.inline_object6 import InlineObject6
from vrchatapi.model.inline_object7 import InlineObject7
from vrchatapi.model.inline_object8 import InlineObject8
from vrchatapi.model.inline_object9 import InlineObject9
from vrchatapi.model.inline_response200 import InlineResponse200
from vrchatapi.model.inline_response2001 import InlineResponse2001
from vrchatapi.model.inline_response2002 import InlineResponse2002
from vrchatapi.model.inline_response2003 import InlineResponse2003
from vrchatapi.model.inline_response2004 import InlineResponse2004
from vrchatapi.model.inline_response2005 import InlineResponse2005
from vrchatapi.model.inline_response2006 import InlineResponse2006
from vrchatapi.model.inline_response400 import InlineResponse400
from vrchatapi.model.instance import Instance
from vrchatapi.model.instance_platforms import InstancePlatforms
from vrchatapi.model.invite_message import InviteMessage
from vrchatapi.model.invite_message_id import InviteMessageID
from vrchatapi.model.invite_message_type import InviteMessageType
from vrchatapi.model.limited_unity_package import LimitedUnityPackage
from vrchatapi.model.limited_user import LimitedUser
from vrchatapi.model.limited_world import LimitedWorld
from vrchatapi.model.mime_type import MIMEType
from vrchatapi.model.notification import Notification
from vrchatapi.model.notification_type import NotificationType
from vrchatapi.model.past_display_name import PastDisplayName
from vrchatapi.model.permission import Permission
from vrchatapi.model.permission_id import PermissionID
from vrchatapi.model.player_moderation import PlayerModeration
from vrchatapi.model.player_moderation_id import PlayerModerationID
from vrchatapi.model.player_moderation_type import PlayerModerationType
from vrchatapi.model.release_status import ReleaseStatus
from vrchatapi.model.response import Response
from vrchatapi.model.success import Success
from vrchatapi.model.tag import Tag
from vrchatapi.model.unity_package import UnityPackage
from vrchatapi.model.unity_package_id import UnityPackageID
from vrchatapi.model.user import User
from vrchatapi.model.user_state import UserState
from vrchatapi.model.user_status import UserStatus
from vrchatapi.model.world import World
from vrchatapi.model.world_id import WorldID
