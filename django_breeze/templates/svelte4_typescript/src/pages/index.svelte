<script lang="ts">
  import PackageCard from '../components/PackageCard.svelte';
  import { page } from '@inertiajs/svelte';

  type Framework = string;

  const packages: Framework[] = $page.props.packages;
</script>

<div class="text-center h-screen flex justify-center flex-col items-center p-4">
  <img
    class="w-full lg:w-[60%]"
    src="/static/django_breeze/django-breeze-logo.jpg"
    alt=""
  />
  <h1 class="text-3xl font-bold">Welcome, Django Breeze</h1>
  <p class="text-green-600 mb-5">Your project is setup successfully!</p>
  <h3 class="text-slate-500">Powered by:</h3>
  <div class="lg:flex space-y-2 lg:space-y-0 lg:space-x-3 mt-3">
    {#each packages as framework}
      <PackageCard framework={framework} />
    {/each}
  </div>
</div>