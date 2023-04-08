const template = `
<nav class="navbar is-fixed-top has-shadow" aria-label="main navigation">
  <div class="container">
  
    <div class="navbar-brand">
      <a class="navbar-item" href="/">
        <img src="/web/assets/logo.svg" class="site-logo" alt="0L-Signals Logo">
        <span class="site-logo-text">0L-Signals</span>
      </a>
  
      <!-- Burger menu: Hidden by default on desktop -->
      <a id="navbar-burger" role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarMenu">
        <span aria-hidden="true"/><span aria-hidden="true"/><span aria-hidden="true"/>
      </a>
    </div>
  
    <div id="navbarMenu" class="navbar-menu">
      <div class="navbar-end">
        <a v-for="link of links" class="navbar-item" :href="link.url" :target="link.url.startsWith('http')? '_blank': ''">
          {{ link.name }}
        </a>
      </div>
    </div>
  </div>
</nav>
`

// https://bulma.io/documentation/components/navbar/
// Enable JS functionality of burger menu
document.addEventListener('DOMContentLoaded', () => {
  // Get "navbar-burger"
  const $navbarBurger = document.getElementById('navbar-burger')
  if ($navbarBurger) {
    $navbarBurger.addEventListener('click', () => {
      // Get the target from the "data-target" attribute
      const target = $navbarBurger.dataset.target
      const $target = document.getElementById(target)
      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      $navbarBurger.classList.toggle('is-active')
      $target.classList.toggle('is-active')
    })
  }
})

export default {
  template,
  data () {
    return {
      links: [
        { name: 'Proposals', url: '/' },
        { name: '0L', url: 'https://0l.network' },
      ],
    }
  },
}
