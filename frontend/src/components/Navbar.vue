<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link 
        :to="{ name: 'Home' }" 
        class="navbar-brand"
        >MyQuora
      </router-link>

      <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item active">
            <router-link
              :to="{ name: 'Home' }" 
              class="btn btn-sm btn-success"
              >Home
            </router-link>
          </li>
          <li class="nav-item mx-3">
            <router-link 
              :to="{ name: 'QuestionEditor' }" 
              class="btn btn-sm btn-danger"
              >Ask Question
            </router-link>
          </li>
          <li class="nav-item">
            <a class="btn btn-sm btn-outline-secondary" href="/accounts/logout/"
              >Logout
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<style>
.my-navbar {
  border-bottom: 1px solid #ddd;
}
</style>
