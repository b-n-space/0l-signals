const template = `
<!-- Allow passing another class to switch the color -->
<header class="hero" :class="color || 'is-primary'">
  <div class="hero-body content">
    <div class="container">
      <!-- Allow passing another tag in case h1 is not the right one for the title -->
      <component :is="tag || 'h1'" class="title">{{ title }}</component>
      <p class="subtitle">{{ subtitle }}</p>
    </div>
  </div>
</header>
`;

export default {
  template,
  // Expected properties to be passed to the component
  // <ps-hero tile="text" ...></ps-hero>, or for dynamic vars
  // <ps-hero :tile="someJSVar" ...></ps-hero>
  props: ["title", "subtitle", "color", "tag"],
};
