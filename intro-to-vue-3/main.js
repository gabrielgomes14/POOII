const { createApp, ref } = Vue;

const app = createApp({
  setup() {
    const product = ref("Socks");
    const image = ref("assets/socks_green.jpg"); // Use / em vez de \
    const url = ref("https://www.linkedin.com/in/gabriel-gomes-574287258/");
    
    return {
      product, image, url
    }
  }
});
