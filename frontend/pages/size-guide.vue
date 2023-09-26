<script lang="ts" setup>
definePageMeta({
  layout: 'default-line-header',
})
</script>


<template>
  <div class="mt-5 mb-24 container mx-auto">
    <div><UButton label="GO BACK" icon="i-ph-arrow-up-left" to="/" variant="ghost" color="gray" /></div>
    <div class="my-5 flex gap-5">
      <div class="w-1/3 text-center">
        <div class="text-4xl">SIZE GUIDE</div>
        <div class="my-5 text-xl">THE CHART BELOW PROVIDES DETAILED MEASUREMENTS OF THIS GARMENT</div>
        <div>
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
      <div class="w-2/3 text-center">
        <div class="text-4xl">SIZE CONVERSION</div>
        <div class="my-5 text-xl">INTERNATIONAL SIZING CONVERSIONS <br> TO HELP SELECT YOUR CORRECT SIZE</div>
        <div>
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

td, th {
  border: 2px solid #dddddd;
  text-align: center;
  padding: 8px;
}

</style>