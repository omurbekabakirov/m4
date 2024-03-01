"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views. home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from product.views import (
    hello_view,
    current_date_view,
    goodbye_view,
    product_list_view,
    main_view,
    product_detail_view,
    create_product_view,
    create_category_view
)
from users.views import (
    register_view,
    login_view,
    profile_view,
    logout_view,
    confirm_view

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main_view'),
    path('hello/', hello_view),
    path('current_date/', current_date_view),
    path('goodbye/', goodbye_view),
    path('products/', product_list_view),
    path('products/<int:product_id>/', product_detail_view),
    path('products/create/', create_product_view),
    path('products/create_category/', create_category_view),

    path('register/', register_view),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, ),
    path('logout/', logout_view),
    path('confirm/<str:code>/', confirm_view, name='confirm')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
