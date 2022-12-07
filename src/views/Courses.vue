<template>
  <div class="courses">
    <div class="hero is-info">
      <div class="hero-body has-text-centered has-background-grey-darker">
        <h1 class="title">Courses</h1>
      </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="columns">

                <div class="column is-2">
                    <aside class="menu">
                        <p class="menu-label">Categories</p>

                        <ul class="menu-list">
                            <li><a class="is-active" href="">All courses</a></li>
                            <li><a href="">Machine Learning</a></li>
                            <li><a href="">Mathematics</a></li>
                            <li><a href="">Programming</a></li>
                        </ul>
                    </aside>
                </div>

                <div class="column is-10">
                    <div class="columns is-multiline">
                        <div 
                            class="column is-4" 
                            v-for="course in courses"
                            v-bind:key="course.id"
                        >
                            <CourseItem :course="course" />
                        </div>

                        <div class="column is-12">
                            <nav class="pagination">
                                <a class="pagination-previous">Previous</a>
                                <a class="pagination-next" href="">Next</a>
                                <ul class="pagination-list">
                                    <li>
                                        <a class="pagination-link is-current" href="">1</a>
                                    </li>
                                    <li>
                                        <a class="pagination-link" href="">2</a>
                                    </li>
                                    <li>
                                        <a class="pagination-link" href="">3</a>
                                    </li>
                                </ul>
                            </nav>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
  </div>
</template>


<script>
import axios from 'axios'
import CourseItem from '@/components/CourseItem.vue'

export default {
    data() {
        return {
            courses: []
        }
    },
    components: {
        CourseItem
    },
    mounted() {
        console.log('mounted')

        axios
            .get('/api/v1/courses')
            .then(response => {
                console.log(response.data)

                this.courses = response.data
            })
    }
}
</script>