from django.urls import path, re_path

from book.views.v1 import views as v1_view
from book.views.v2 import views as v2_view
from book.views.v3 import views as v3_view
from book.views.v4 import views as v4_view
from book.views.v5 import views as v5_view


urlpatterns = [
    # FBV django
    path('v1/publish', v1_view.PublishView),
    # CBV View Django
    path('v1/publish_v1', v1_view.PublishViewV2.as_view()),
    path('v1/publish_v3', v1_view.PublisherViewV3.as_view()),
    path('v1/publish_v3/<int:pk>', v1_view.PublisherViewV3.as_view()),

    # drf APIView
    path('v2/publish_v1', v2_view.PublishViewV1.as_view()),
    path('v2/publish_v2/', v2_view.PublishViewV2.as_view()),
    path('v2/publish_v2/<int:pk>/', v2_view.PublishViewV2.as_view()),

    # drf APIView book
    path('v2/book', v2_view.BookAPIView.as_view()),

    # Parse 解析器
    path('v3/parse', v3_view.ParseAPIView.as_view()),
    path('v3/render', v3_view.ParseAPIView.as_view()),

    # GenericAPIView
    path('v4/publisher/', v4_view.PublishGenericAPIView.as_view()),
    path('v4/publisher/<int:pk>/', v4_view.PublishGenericAPIView.as_view()),
    path('v4/book/', v4_view.BookGenericAPIView.as_view()),
    path('v4/book/<int:pk>/', v4_view.BookGenericAPIView.as_view()),

    # mixins + GenericAPIView
    path('v5/publisher/', v4_view.PublishMixinGenericAPIView.as_view()),
    path('v5/publisher/<int:pk>/', v4_view.PublishMixinGenericAPIView.as_view()),

    # GenericAPIView + mixins
    path('v6/publisher/', v4_view.PublishV2MixinGenericAPIView.as_view()),
    path('v6/publisher/<int:pk>/', v4_view.PublishV2MixinGenericAPIView.as_view()),

    # GenericAPIView + mixins
    path('v7/publisher/', v4_view.PublishViewSet.as_view(
        {
            "get": "list",
            "post": "create",
        }
    )),
    path('v7/publisher/<int:pk>/', v4_view.PublishViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "delete": "destroy",
        }
    )),

    # GenericAPIView + mixins
    path('v8/publisher/', v4_view.PublishModelViewSet.as_view(
        {
            "get": "list",
            "post": "create",
        }
    )),
    path('v8/publisher/<int:pk>/', v4_view.PublishModelViewSet.as_view(
        {
            "get": "retrieve",
            "put": "update",
            "delete": "destroy",
        }
    )),

    # 认证
    path('v9/auth_1/', v3_view.Auth1APIView.as_view()),
    path('v9/auth_2/', v3_view.Auth2APIView.as_view()),
    path('v9/auth_3/', v3_view.Auth3APIView.as_view()),

    # 分页
    path('v10/publisher/', v4_view.PublishGenericAPIView.as_view()),
    path('v10/publisher/<int:pk>/', v4_view.PublishGenericAPIView.as_view()),

    # test
    path('v11/test_perm/', v5_view.TestPermission.as_view()),

]