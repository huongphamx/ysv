<script lang="ts" setup>
definePageMeta({
  layout: 'default-line-header',
})

useHead({
  title: 'Size Guide - YSV'
})
</script>


<template>
  <div class="mt-5 mb-24 mycontainer mx-auto">

    <div class="hidden lg:flex items-center gap-2 hover:cursor-pointer" @click="$router.back()">
      <UIcon name="i-ph-arrow-up-left" class="text-xl" /><span>GO BACK</span>
    </div>

    <div class="my-5 2xl:flex">
      <div class="my-5 text-center 2xl:w-1/3">
        <div class="text-xl md:text-3xl lg:text-4xl font-['Italiana']">SIZE GUIDE</div>
        <div class="my-5 text-sm md:text-lg 2xl:text-xl">THE CHART BELOW PROVIDES DETAILED MEASUREMENTS OF THIS GARMENT
        </div>
        <div class="text-xs sm:text-sm md:text-base">
          <table class="w-full">
            <tr>
              <th>SIZE</th>
              <th>BUST</th>
              <th>WAIST</th>
              <th>HIPS</th>
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
      </div>
      <div class="my-5 text-center 2xl:w-2/3">
        <div class="text-xl md:text-3xl lg:text-4xl font-['Italiana']">SIZE CONVERSION</div>
        <div class="my-5 text-sm md:text-lg 2xl:text-xl">INTERNATIONAL SIZING CONVERSIONS <br> TO HELP SELECT YOUR CORRECT
          SIZE</div>
        <div class="text-[8px] md:text-base">
          <table class="w-4/5 mx-auto">
            <tr>
              <th>SIZE</th>
              <th>US</th>
              <th>UK/AUS</th>
              <th>FRANCE</th>
              <th>ITALY</th>
              <th>JAPAN</th>
              <th>DENMARK</th>
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
  </div>
</template>


<style scoped>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
}

td,
th {
  border: 2px solid #dddddd;
  text-align: center;
  padding: 8px;
}
</style>