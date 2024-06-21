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
      path: '/list_technicians',
      name: 'listTechnicians',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ListTechniciansView.vue')
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
      path: '/file/create',
      name: 'createFile',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FileCreateView.vue')
    },
    {
      path: '/file/createLoc',
      name: 'createLocFile',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FileCreateLocView.vue')
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
      path: '/file/:id/create_tech_measurement',
      name: 'createTechMeasurement',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FormTMView.vue')
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
      path: '/file/:id/tech_measurement',
      name: 'tech_measurement',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/TechMeasurementDisplayView.vue')
    },
    {
      path: '/station',
      name: 'station',
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
      path: '/list_non_ionizing_radiation',
      name: 'listNIR',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/ListNIRMeasurementsView.vue')
    },
    {
      path: '/non_ionizing_radiation/create',
      name: 'createNIR',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/FormNewNIRMeasurementView.vue')
    },
    {
      path: '/non_ionizing_radiation/:id',
      name: 'deleteNIR',
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
  ]
})

export default router
