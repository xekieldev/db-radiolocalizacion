import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/change_password',
      name: 'changePassword',
      component: () => import('../views/ChangePassView.vue')
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/list',
      name: 'list',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ListView.vue')
    },
    {
      path: '/file/create',
      name: 'newFile',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FormNewFileView.vue')
    },
    {
      path: '/file/:id',
      name: 'file',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FileDisplayView.vue')
    },
    {
      path: '/file/:id/edit',
      name: 'editFile',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FileEditView.vue')
    },
    {
      path: '/list_technicians',
      name: 'listTechnicians',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ListTechniciansView.vue')
    },
    {
      path: '/file/:file_id/station/:id',
      name: 'station',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/StationDisplayView.vue')
    },
    {
      path: '/file/:file_id/station/:id/edit',
      name: 'editStation',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/StationEditView.vue')
    },
    {
      path: '/file/:id/station/create',
      name: 'createStation',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/StationCreateView.vue')
    },
    {
      path: '/file/:id/station/createLoc',
      name: 'createLocStation',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/StationCreateLocView.vue')
    },
    {
      path: '/technician/create_technician',
      name: 'createTechnician',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FormNewTechnicianView.vue')
    },
    {
      path: '/file/:file_id/station/:id/create_tech_measurement',
      name: 'createTechMeasurement',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FormTMView.vue')
    },
    {
      path: '/file/:file_id/activity',
      name: 'createActivity',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FileDisplayView.vue')
    },
    {
      path: '/technician/:id/delete_technician',
      name: 'deleteTechnician',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FormDeleteTechnicianView.vue')
    },
    {
      path: '/file/:file_id/station/:id/tech_measurement',
      name: 'tech_measurement',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/TechMeasurementDisplayView.vue')
    },
    {
      path: '/station',
      name: 'stations',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ListStationsView.vue')
    },
    {
      path: '/station_map',
      name: 'map',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/MapStationsView.vue')
    },
    {
      path: '/files_map',
      name: 'filesMap',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/MapFilesView.vue')
    },
    {
      path: '/list_non_ionizing_radiation',
      name: 'listNIR',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ListNIRMeasurementsView.vue')
    },
    {
      path: '/file/:file_id/non_ionizing_radiation/create',
      name: 'createNIR',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FormNewNIRMeasurementView.vue')
    },
    {
      path: '/file/:file_id/non_ionizing_radiation/:id',
      name: 'viewNIRMeasurement',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/NirMeasDisplayView.vue')
    },
    {
      path: '/nir_map',
      name: 'nirMap',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/MapNirView.vue')
    }, 
    {
      path: '/statistics',
      name: 'statistics',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/StatisticsView.vue')
    }, 
  ]
})
// router.beforeEach((to, from, next) => {
//   if(to.name === 'stations') {
//     next({name: 'login'})
//   }
//   else {
//     next()
//   }
// });
export default router
