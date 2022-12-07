<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/> -->

    <div class="hero is-info is-medium has-background-grey-darker">
      <div class="hero-body has-text-centered">
        <h1 class="title">Welcome to HappyStudy</h1>
        <h2 class="subtitle">An online place for learning what you want</h2>
      </div>
    </div>

    <section class="section">
      <div class="container">
        <div class="columns is-multiline">

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-clock"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study at your own pace</h2>
              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="far fa-comments"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study with others</h2>
              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-4">
            <div class="box has-text-centered">
              <span class="icon is-size-2 has-text-info"><i class="fas fa-home"></i></span>
              <h2 class="is-size-4 mt-4 mb-4">Study from your home</h2>
              <p>This is just some random placeholder text</p>
            </div>
          </div>

          <div class="column is-12 has-text-centered">
            <a href="/courses" class="button is-info is-size-3 mt-6 mb-6">Click here to get started</a>
          </div>
          
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// // @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "HomeView",
  // components: {
  //   HelloWorld
  // }
};
</script>
