
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.authentication_api import AuthenticationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from vrchatapi.api.authentication_api import AuthenticationApi
from vrchatapi.api.avatars_api import AvatarsApi
from vrchatapi.api.economy_api import EconomyApi
from vrchatapi.api.favorites_api import FavoritesApi
from vrchatapi.api.files_api import FilesApi
from vrchatapi.api.friends_api import FriendsApi
from vrchatapi.api.instances_api import InstancesApi
from vrchatapi.api.invite_api import InviteApi
from vrchatapi.api.notifications_api import NotificationsApi
from vrchatapi.api.permissions_api import PermissionsApi
from vrchatapi.api.playermoderation_api import PlayermoderationApi
from vrchatapi.api.system_api import SystemApi
from vrchatapi.api.users_api import UsersApi
from vrchatapi.api.worlds_api import WorldsApi
