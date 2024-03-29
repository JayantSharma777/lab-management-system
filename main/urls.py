from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name='main'

urlpatterns = [
    # auth paths
    path("accounts/signup/", views.register_request, name="register"),
    path('accounts/email-confirmation/<uidb64>/<token>', views.activate_user, name='active_email'),
    path("accounts/login/", views.login_request, name="login"),
    path("accounts/logout/<id>", views.logout_request, name= "logout_request"),
    path('accounts/password-reset/', views.passwordResetView, name="passwordReset"),
    path('accounts/password-reset/<uidb64>/<token>/', views.passwordResetConfirmView, name="passwordResetConfirm"),
    path('accounts/password-reset/<token>/<id>', views.passwordResetForm, name="passwordResetForm"),
    path('accounts/password-change/<id>', views.passwordChange, name="passwordChange"),
 
    # user paths
    path('', views.user_profile, name='home'),
    path('profile/user-profile/' ,views.user_profile, name='user_profile'),
    path('profile/user-profile-details/',views.user_profile_details, name='userProfileDetails'),
    path('profile/edit-profile/<pk>',views.editProfile, name='editProfile'),
    path('complaint/<pk>',views.complaint, name='complaint'),
    path("lab/<pk>", views.lab, name='lab'),
    path('lab/view_lab_devices/<device_type>/<lab>',views.view_lab_devices,name='view_lab_devices'),
    path('lab/expire-device/<id>',views.expire_lab_device,name='expire_lab_device'),
    path('lab/view-expired-devices/<pk>',views.view_expired_lab_devices,name='view_expired_lab_devices'),
    path("add/<pk>",views.add_devices,name='add_devices'),
    path('complaint-resolve/<pk>', views.resolveConflict, name='resolveConflict'),
    path('profile/leaves/', views.userLeaves, name="userLeaves"),
    path('profile/leaves/request-leaves', views.requestleave, name="requestleave"),
    path('profile/notifications/', views.notifications, name='notification'),
    path('profile/notification/<pk>', views.handleNotification, name="handleNotification"),
    path('profile/leaves/check-leave-status/', views.checkLeaveStatus, name='checkLeaveStatus'),
    path('profile/leaves/check-leave-status/<pk>' , views.checkLeaveStatusId, name="currleaveStatus"),
    path('profile/leaves/check-leave-status/cancel/<pk>', views.cancelLeaveRequest, name='cancelLeaveRequest'),
    path('profile/leaves/approve-leaves/', views.approveLeaves, name='approveLeaves'),
    path('profile/leaves/approve-leaves/approve/<pk>', views.approveRequest, name='approveRequest'),
    path('profile/leaves/approve-leaves/decline/<pk>', views.declineRequest, name='declineRequest'),
    path('dashboard/view-complaints/' , views.view_complaints, name="viewcomplaints"),
    path('dashboard/previous-leaves/',views.viewprevleaves,name='viewprevleaves'),
    path('dashboard/courses/',views.viewcourses,name='viewcourses'),
    path('dashboard/groups/',views.viewgroups,name='viewgroups'),
    path('dashboard/group-courses/',views.viewgroupcourses,name='viewgroupcourses'),
    path('dashboard/classes/',views.viewfacultyclasses,name='viewfacultyclasses'),
    path('dashboard/faculty-timetable/<id>',views.viewfacultytimetable,name='viewfacultytimetable'),
    path('dashboard/items-alloted/',views.viewinventory,name='viewinventory'),
    path('darshboard/add-faculty', views.addFaculty, name="addFaculty"),
    path('comlpaints/escalate/<pk>', views.escalation, name="escalate"),

    # admin paths
    path('admin-dashboard/leaves/requested-leaves', views.adminRequestedLeaves, name='adminRequestedLeaves'),
    path('admin-dashboard/leaves/rejected-leaves', views.adminRejectedLeaves, name='adminRejectedLeaves'),
    path('admin-dashboard/leaves/approved-leaves', views.adminApprovedLeaves, name='adminApprovedLeaves'),
    path('admin-dashboard/staff-members-list/', views.adminStaff, name='adminStaff'),
    path('admin-dashboard/staff-members-list/edit_profile/<id>', views.admineditstaffprofile, name='admineditstaffprofile'),
    path('admin-dashboard/view-inventory/<id>',views.adminviewinventory,name='adminviewinventory'),
    path('admin-dashboard/view-inventory/approveDeviceRequest/<pk>',views.approveDeviceRequest,name='approveDeviceRequest'),
    path('admin-dashboard/view-inventory/declineDeviceRequest/<pk>',views.declineDeviceRequest,name='declineDeviceRequest'),
    path('admin-dashboard/current-year-leaves/', views.adminLeaves, name='adminLeaves'),
    path('admin-dashboard/current-year-leaves/new-leave-form', views.newLeave, name='newLeave'),
    path('admin-dashboard/leaves-history/', views.leaveUsersHistory, name='leaveUsersHistory'),
    path('admin-dashboard/current-year-leaves/leave/<pk>', views.adminEditLeave, name='adminEditLeave'),
    path('admin-dashboard/current-year-leaves/remove-leave/<pk>', views.removeLeave, name='removeLeave'),
    path('admin-dashboard/labs-list/', views.adminLabs, name='adminLabs'),
     path('admin-dashboard/labs-list/edit-lab/<pk>', views.admineditlab, name='admineditlab'),
    path('admin-dashboard/labs-list/add-lab', views.adminaddlab, name='adminaddlab'),
    path('admin-dashboard/rooms/', views.adminviewrooms, name='adminviewrooms'),
    path('admin-dashboard/rooms/add-room/', views.adminaddroom, name='adminaddroom'),
    path('admin-dashboard/rooms/edit-room/<id>', views.admineditroom, name='admineditroom'),
    path('admin-dashboard/courses/', views.viewallcourses, name='viewallcourses'),
    path('admin-dashboard/courses/add-Course/', views.adminaddcourse, name='adminaddcourse'),
    path('admin-dashboard/courses/edit-Course/<id>', views.admineditcourse, name='admineditcourse'),
    path('admin-dashboard/groups/', views.viewallgroups, name='viewallgroups'),
    path('admin-dashboard/groups/add-group/', views.addgroup, name='addgroup'),
    path('admin-dashboard/groups/edit-group/<id>', views.admineditgroup, name='admineditgroup'),
    path('admin-dashboard/complaints-list/', views.adminComplaints, name='adminComplaints'),
    path('admin-dashboard/complaints-list/Active-Complaints', views.adminactivecomplaints, name='adminactivecomplaints'),
    path('admin-dashboard/complaints-list/Resolved-Complaints', views.adminresolvedcomplaints, name='adminresolvedcomplaints'),
    path('admin-dashboard/faculty-details/',views.ViewFacultyDetails,name='adminfacultydetails'),
    path('admin-dashboard/faculty-details/admin-view-groups/<id>',views.adminviewgroups,name='adminviewgroups'),
    path('admin-dashboard/faculty-details/admin-view-courses/<id>',views.adminviewcourses,name='adminviewcourses'),
    path('admin-dashboard/faculty-details/admin-view-group-courses/<id>',views.adminviewgroupcourses,name='adminviewgroupcourses'),
    path('admin-dashboard/faculty-details/admin-view-group-courses/add-group-course/<id>',views.adminaddgroupcourse,name='adminaddgroupcourse'),
    path('admin-dashboard/faculty-details/admin-view-classes/<id>',views.adminviewclasses,name='adminviewclasses'),
    path('admin-dashboard/faculty-details/admin-view-groups/delete-group/<id>',views.admindeletegroup,name='admindeletegroup'),
    path('admin-dashboard/faculty-details/admin-view-courses/delete-courses/<id>',views.admindeletecourses,name='admindeletecourses'),
    path('admin-dashboard/faculty-details/admin-view-courses/delete-group-courses/<id>',views.admindeletegroupcourse,name='admindeletegroupcourse'),
    path('admin-dashboard/faculty-details/admin-view-courses/add-course/<id>',views.adminaddcourses,name='adminaddcourses'),
    path('admin-dashboard/faculty-details/admin-view-courses/add-group/<id>',views.adminaddgroup,name='adminaddgroup'),
    path('admin-dashboard/faculty-details/admin-view-courses/add-faculty-class/<id>',views.adminaddfacultyclass,name='adminaddfacultyclass'),
    path('admin-dashboard/faculty-details/admin-view-courses/update-faculty-class/<id><pk>',views.adminupdatefacultyclass,name='adminupdatefacultyclass'),
    path('admin-dashboard/faculty-details/admin-view-courses/delete-class/<id>',views.admindeleteclass,name='admindeleteclass'),
    path('admin-dashboard/faculty-details/admin-view-courses/delete-faculty-class/<id>',views.admindeletefacultyclass,name='admindeletefacultyclass'),
    path('admin-dashboard/assign-office/', views.adminassignoffice, name='adminassignoffice'),
    path('admin-dashboard/branches/', views.adminviewbranches, name='adminviewbranches'),
    path('admin-dashboard/branches/add-branch', views.adminaddbranch, name='adminaddbranch'),
    path('admin-dashboard/branches/edit-branch/<id>', views.admineditbranch, name='admineditbranch'),
    path('admin-dashboard/type-of-devices/', views.adminviewTypeOfDevices, name='adminviewTypeOfDevices'),
    path('admin-dashboard/type-of-devices/add-type-of-device', views.adminaddTypeOfDevice, name='adminaddTypeOfDevice'),
    path('admin-dashboard/type-of-devices/edit-type-of-device/<id>', views.admineditTypeOfDevice, name='admineditTypeOfDevice'),
    path('admin-dashboard/Assign-office/load_previous_assigned_staff',views.load_prev_assigned_offices,name='ajax_load_prev_assigned_offices'),
    path('admin-dashboard/view-devices',views.adminviewdevices,name='adminviewdevices'),
    path('admin-dashboard/view-devices/delete-device/<id>',views.admin_delete_device,name='admin_delete_device'),
    path('admin-dashboard/view-devices/view-warehouse-devices',views.adminview_warehouse_devices,name='adminview_warehouse_devices'),
    path('admin-dashboard/view-devices/view-assigned-devices',views.adminview_assigned_devices,name='adminview_assigned_devices'),
    path('admin-dashboard/view-devices/view-assigned-devices/add-device/',views.adminadd_device,name='adminadd_device'),
    path('admin-dashboard/view-devices/view-warehouse-devices/add-device/',views.adminadd_warehouse_device,name='adminadd_warehouse_device'),
    path('admin-dashboard/view-devices/view-warehouse-devices/edit-device/<id>',views.adminedit_warehouse_device,name='adminedit_warehouse_device'),
    path('admin-dashboard/view-devices/view-assigned-devices/edit-device/<id>',views.adminedit_assigned_device,name='adminedit_assigned_device'),
    
    #timetable paths
    path('timetable/view-lab/<id>',views.viewtimetable_wrtlab,name='viewtimetable_wrtlab'),
    path('timetable/view-lab-classes/<id>',views.viewLabClasses,name='viewLabClasses'),
    path('timetable/add_class/<id>',views.add_classes,name = 'add_classes'),
    path('timetable/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX
    path('timetable/load-groups/', views.load_groups, name='ajax_load_groups'),
    path('timetable/load-group-courses/', views.load_groupcourses, name='ajax_load_groupcourses'), # AJAX
    path('timetable/updateclass/<pk>_<id>/', views.update_class, name='update_class'),
    path('timetable/view-all-faculty-courses/<id>/',views.viewallfacultycourses,name='viewallfacultycourses'),
    path('timetable/view-all-faculty-groups/<id>/',views.viewallfacultygroups,name='viewallfacultygroups'),
    path('timetable/view-all-faculty-group-courses/<id>/',views.viewallfacultygroupcourses,name='viewallfacultygroupcourses'),
    path('timetable/view-all-faculty-Classes/<id>/',views.viewallfacultyclasses,name='viewallfacultyclasses'),

    #inventory paths
    path('inventory/allot-devices/<id>',views.allotdevices,name='allotdevices'),
    path('inventory/load-devices/<id>', views.loaddevices, name='ajax_load_devices'), # AJAX
    path('inventory/return-devices/<id>',views.devicesreturnrequest,name='devicesreturnrequest'),
    path('inventory/inventory-logs/',views.viewinventorylogs,name='viewinventorylogs'),
    path('inventory/view-expired-inventory-devices/',views.view_expired_inventory_devices,name='view_expired_inventory_devices'),
    path('inventory/view-inventory-devices/<device_type>',views.view_inventory_devices,name='view_inventory_devices'),
    path('inventory/view-inventory-devices/expire-inventory-device/<id>',views.expire_inventory_devices,name='expire_inventory_device'),
    path('complaints/viewdevicecomplaints/<id>',views.viewdevicecomplaints,name='viewdevicecomplaints')
]
