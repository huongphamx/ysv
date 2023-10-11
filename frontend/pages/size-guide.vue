<script lang="ts" setup>
const isShowedHeaderLine = useIsShowedHeaderLine()
isShowedHeaderLine.value = true

useHead({
  title: 'Size Guide - YSV'
})
</script>


<template>
  <div class="sizeguide-body mycontainer mx-auto">
    <GoBackArrow />
    <div class="mb-5 xl:flex justify-between">
      <div class="mb-5 text-center">
        <div class="text-medium">SIZE GUIDE</div>
        <div class="table-description mx-auto text-small max-w-[390px]">THE CHART BELOW PROVIDES DETAILED MEASUREMENTS OF
          THIS
          GARMENT
        </div>
        <table class="table-guide">
          <tr>
            <td>SIZE</td>
            <td>BUST</td>
            <td>WAIST</td>
            <td>HIPS</td>
          </tr>
          <tr>
            <td>XS</td>
            <td>83-86</td>
            <td>63-66</td>
            <td>90-93</td>
          </tr>
          <tr>
            <td>S</td>
            <td>86-89</td>
            <td>66-69</td>
            <td>93-96</td>
          </tr>
          <tr>
            <td>M</td>
            <td>89-92</td>
            <td>69-72</td>
            <td>96-99</td>
          </tr>
          <tr>
            <td>L</td>
            <td>92-95</td>
            <td>72-75</td>
            <td>99-102</td>
          </tr>
        </table>
      </div>
      <div class="mb-5 text-center">
        <div class="mt-10 xl:mt-0 text-medium">SIZE CONVERSION</div>
        <div class="table-description text-small">INTERNATIONAL SIZING CONVERSIONS <br> TO HELP SELECT YOUR CORRECT
          SIZE</div>
        <table class="table-conversion">
          <tr>
            <td>SIZE</td>
            <td>US</td>
            <td>UK/AUS</td>
            <td>FRANCE</td>
            <td>ITALY</td>
            <td>JAPAN</td>
            <td>DENMARK</td>
          </tr>
          <tr>
            <td>XS</td>
            <td>0-2</td>
            <td>6</td>
            <td>34</td>
            <td>38</td>
            <td>5</td>
            <td>32</td>
          </tr>
          <tr>
            <td>S</td>
            <td>2-4</td>
            <td>8</td>
            <td>36</td>
            <td>40</td>
            <td>7</td>
            <td>34</td>
          </tr>
          <tr>
            <td>M</td>
            <td>6-8</td>
            <td>10</td>
            <td>38</td>
            <td>42</td>
            <td>9</td>
            <td>36</td>
          </tr>
          <tr>
            <td>L</td>
            <td>8-10</td>
            <td>12</td>
            <td>40</td>
            <td>44</td>
            <td>11</td>
            <td>38</td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>


<style scoped>
.sizeguide-body {
  margin-bottom: 50px;

  @media screen and (min-width: 480px) {
    margin-bottom: 80px;
  }

  @media screen and (min-width: 768px) {
    margin-bottom: 100px;
  }

  @media screen and (min-width: 1280px) {
    margin-bottom: 150px;
  }
}

.table-description {
  width: 264px;
  margin: 15px auto;

  @media screen and (min-width: 480px) {
    width: 341px;
    margin: 20px auto;
  }

  @media screen and (min-width: 1280px) {
    width: 400px;
  }
}

table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  table-layout: fixed;
  margin: 0 auto;
}

td,
th {
  border: 2px solid #888888;
  text-align: center;
  padding: 14px 0;
}

.table-guide {
  font-size: 14px;
  width: 300px;

  @media screen and (min-width: 480px) {
    width: 390px;
  }

  @media screen and (min-width: 1280px) {
    width: 400px;
    font-size: 16px;
  }
}

.table-conversion {
  font-size: 8px;
  width: 300px;

  @media screen and (min-width: 480px) {
    font-size: 10px;
    width: 420px;
  }

  @media screen and (min-width: 768px) {
    font-size: 14px;
    width: 618px;
  }

  @media screen and (min-width: 1280px) {
    font-size: 16px;
    width: 681px;
  }
}
</style>