const container = document.querySelector(".weather-content");

const temperatureBox = document.querySelector(".tempr");
const weatherStatus = document.querySelector(".status");
const weatherPic = document.querySelector(".weather-image");
const form = document.querySelector("#form");

const statusImages = {
  sunny:
    "https://media.gettyimages.com/id/1135378306/photo/sunny-day.jpg?s=612x612&w=0&k=20&c=_pAlDJoRVKJYt68rrcSj5WUgjv8ju-QgXZYuGdpNtxg=",
  rainy: "https://www.pngmart.com/files/22/Raining-PNG-Pic.png",
  snow: "https://imgs.search.brave.com/QV4orQ6s_ypnOck0zTkysl_DwybVdJMhANIcXjnh1GA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jbGlw/YXJ0LWxpYnJhcnku/Y29tL2ltYWdlX2dh/bGxlcnkvbjc3MjY3/Mi5wbmc",
  foggy:
    "https://imgs.search.brave.com/SGuqoIfOwXdqgStY2it2W2F2KVEeTQhhGb0qrFIhsJo/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL3RodW1icy81/OGFmMDM4YTZjMjUy/NDk5MjgxYWU5MWMu/cG5n",
  cloudy:
    "https://imgs.search.brave.com/SaLX4x2l7eHP42o2tA7R61N9EJTUhV2NMljnolPld3k/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9wbHVz/cG5nLmNvbS9pbWct/cG5nL3BhcnRseS1j/bG91ZHktcG5nLWhk/LWRvd25sb2FkLXBu/Z3RyYW5zcGFyZW50/LTMxOS5wbmc",
};

fetch("./weather.json")
  .then((res) => {
    return res.json();
  })
  .then((data) => {
    temperatureBox.innerHTML = `${data.temperature} ${data.temperatureUnit}`;
    weatherPic.style.backgroundImage = `url(${statusImages[data.status]})`;
  });

form.addEventListener("submit", (e) => {
  e.preventDefault();

  console.log(e.long.value)
});
