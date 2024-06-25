import { createWebHistory, createRouter } from "vue-router";

  const routes =  [
    {
    path: "/login",
    component: () => import('../components/LoginView.vue'),
  },
  {
    path: "/home",
    component: () => import('../components/Veille.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: "/signup",
    component: () => import('../components/Signup.vue'),
  },
  {
    path: "/questions",
    component: () => import('../components/QuestionList.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: "/ask-question",
    component: () => import('../components/AskQuestion.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: "/question/:questionId",
    component: () => import('../components/QuestionDetail.vue'),
    meta: { requiresAuth: true }
  },
  
  

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;