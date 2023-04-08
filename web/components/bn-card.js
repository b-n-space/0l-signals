const template = `
<article class="card">
  <!-- Card content with an optional thumb next to its title -->
  <div class="card-content">
    <a :href="item.link" :title="'Go to ' + item.title">
      <div class="media">
        <!-- Card thumb -->
        <div class="media-left" v-if="item.thumb">
          <figure class="image is-48x48">
            <img :src="item.thumb.src" :alt="item.thumb.alt" />
          </figure>
        </div>
        <!-- Card title -->
        <div class="media-content">
          <h4 class="title is-4">{{ item.title }}</h4>
          <p class="subtitle is-6">{{ item.subtitle }}</p>
        </div>
      </div>
    </a>
    <!-- Card body -->
    <div class="content mt-3">{{ item.body }}</div>
  </div>
  <!-- Card footer to display tags if available -->
  <footer class="card-footer" v-if="item.tags">
    <span class="card-footer-item tags">
      <span v-for="tag in item.tags" class="tag is-primary">{{tag}}</span>
    </span>
  </footer>
</article>
`;

export default {
  template,
  props: ["item"],
};
