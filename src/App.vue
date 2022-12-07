<template>
  <div>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <Nav/>
  <router-view />
  <Footer/>

  </div>
</template>

<script>
import Nav from '@/components/Nav'
import Footer from '@/components/Footer'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    Nav,
    Footer
  },
  beforeCreate() {
    // call the initializeStore from vuex
    this.$store.commit('initializeStore')
    const token = this.$store.state.user.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token "+ token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  }
}
</script>

<style lang="scss">
@import "../node_modules/bulma"; // #app {
//   font-family: Avenir, Helvetica, Arial, sans-serif;
//   -webkit-font-smoothing: antialiased;
//   -moz-osx-font-smoothing: grayscale;
//   text-align: center;
//   color: #2c3e50;
// }

// nav {
//   padding: 30px;

//   a {
//     font-weight: bold;
//     color: #2c3e50;

//     &.router-link-exact-active {
//       color: #42b983;
//     }
//   }
// }
</style>
