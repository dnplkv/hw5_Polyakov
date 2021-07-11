const App = {
    data() {
        return {
            posts: [],
            currentPage: 1,
            hasNext: true,
        }
    },
    delimiters: ['[[', ']]'],
    mounted() {
        this.getPosts();
        window.onscroll = () => {
            let isScrollBottom = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight
            if (isScrollBottom && this.hasNext) {
                this.currentPage++;
                this.getPosts();
            }


        }
    },
    methods: {
        getPosts() {
            fetch(`/api/v1/posts_view/?page=${this.currentPage}`)
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    this.hasNext = data.next !== null;
                    for (let i = 0; i < data.results.length; i++) {
                        this.posts.push(data.results[i]);

                    }
                })

        },
    },
    template: `
        <div v-for='post in posts' :key="post.id" class='list'>
            <h2>[[ post.title ]]</h2>
            <p>[[ post.description ]]</p>
            <a :href="'/posts/'+[[post.id]]+'/'">Read more</a>
        </div>
`,
}
Vue.createApp(App).mount('#app')