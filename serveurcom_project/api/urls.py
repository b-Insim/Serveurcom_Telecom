from django.urls import path
from api.views import PublisherList, PublisherDetail, PublisherComptoiList, PublisherMenuList

urlpatterns = [
    path('references/', PublisherList.as_view()),
    path('bars/ranking/', PublisherComptoiList.as_view()),
    path('menu/', PublisherMenuList.as_view()),
    path('stock/<int:ID_COMPTOIR>/', PublisherDetail.as_view(), name="detail"),
    path('bars/', PublisherList.as_view())
]