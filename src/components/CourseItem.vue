<template>
    <div class="card">
        <div class="card-image">
            <figure class="image is-4by3">
                <!-- <img src="http://bulma.io/images/placeholders/1280x960.png" alt="placeholder image"> -->
                <img src="https://websitehoctructuyen.com/wp-content/uploads/2020/08/e-learning-1024x636.jpg" alt="placeholder image">
            </figure>
        </div>

        <div class="card-content">
            <div class="media">
                <div class="media-content">
                    <p class="is-size-5">{{ course.title }}</p>
                </div>
            </div>

            <div class="content">
                <p>{{ course.short_description}}</p>
                <!-- <a href="#">More</a> -->
                <!-- name=Course refer to Course router -->
                <router-link :to="{name:'Course', params:{slug: course.slug} }">More</router-link>
            </div>

        </div>

    </div>
</template>

<script>

export default {
    props: ['course']
}

</script>