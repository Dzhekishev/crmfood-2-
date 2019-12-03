from django.urls import path
from million import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include
from django.conf.urls import url
urlpatterns=[
path('Table',views.TableView.as_view()),
path('Roles',views.RolesView.as_view()),
path('Deparments',views.DepartmentsView.as_view()),
path('Users',views.UsersView.as_view()),
path('Meal_Categories',views.Meal_CategoriesView.as_view()),
path('Statuses',views.StatusesView.as_view()),
path('ServicePercentage',views.ServicePercentageView.as_view()),
path('Meals',views.MealsView.as_view()),
#path('Orders',views.OrdersView.as_view()),
#path('Checks',views.ChecksView.as_view()),
#path('Meals_to_Order',views.Meals_to_orderView.as_view()),
path('Table/<int:pk>',views.Tabledetails.as_view()),
path('Roles/<int:pk>',views.Rolesdetails.as_view()),
path('Deparments/<int:pk>',views.Departmentsdetails.as_view()),
path('Users/<int:pk>',views.Usersdetails.as_view()),
path('Meal_Categories/<int:pk>',views.Meal_Categoriesdetails.as_view()),
path('Statuses/<int:pk>',views.Statusesdetails.as_view()),
path('Meals/<int:pk>',views.Mealsdetails.as_view()),
#path('Orders/<int:pk>',views.Ordersdetails.as_view()),
#path('Checks/<int:pk>',views.Checksdetails.as_view()),
#path('Meals_to_Order/<int:pk>',views.Meals_to_orderdetails.as_view()),
path('users/', views.UserList.as_view()),
path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns=format_suffix_patterns(urlpatterns)
