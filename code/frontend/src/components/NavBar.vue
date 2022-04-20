<!-- Navigation Header Template -->

<template>
  <Popover class="z-10 relative bg-white dark:bg-gray-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6">
      <div
        class="flex justify-between items-center border-b-2 border-gray-700 py-6 md:justify-start md:space-x-10"
      >
        <div
          class="flex justify-start lg:w-0 lg:flex-1 cursor-pointer"
          @click="goToHome"
        >
          <a>
            <span class="sr-only">Logo</span>
            <p class="text-gray-900 dark:text-gray-200">Logo</p>
            <!-- Replace with our logo img when ready: <img class="h-8 w-auto sm:h-10" src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg" alt="" /> -->
          </a>
        </div>
        <div class="-mr-2 -my-2 md:hidden">
          <PopoverButton
            class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:bg-slate-800 dark:hover:bg-gray-900 dark:hover:text-gray-300"
          >
            <span class="sr-only">Open menu</span>
            <MenuIcon class="h-6 w-6" aria-hidden="true" />
          </PopoverButton>
        </div>
        <PopoverGroup as="nav" class="hidden md:flex space-x-10">
          <Popover class="relative" v-slot="{ open }">
            <PopoverButton
              :class="[
                open
                  ? 'text-gray-900 dark:text-gray-200'
                  : 'text-gray-500 dark:text-gray-400',
                'group bg-white dark:bg-gray-800 rounded-md inline-flex items-center text-base font-medium hover:text-gray-900 dark:hover:text-gray-200',
              ]"
              @click="goToCourses"
            >
              <span>Find Courses</span>
            </PopoverButton>
          </Popover>

          <a
            :href="repoUrl"
            target="_blank"
            class="text-base font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200"
            >Docs</a
          >
          <a
            href="#"
            class="text-base font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200"
            >About</a
          >

          <Popover class="relative" v-slot="{ open }">
            <PopoverButton
              :class="[
                open
                  ? 'text-gray-900 dark:text-gray-200'
                  : 'text-gray-500 dark:text-gray-400',
                'group bg-white dark:bg-gray-800 rounded-md inline-flex items-center text-base font-medium hover:text-gray-900 dark:hover:text-gray-200',
              ]"
              @click="goToMyCourses"
            >
              <span>My Courses</span>
            </PopoverButton>
            <transition
              enter-active-class="transition ease-out duration-200"
              enter-from-class="opacity-0 translate-y-1"
              enter-to-class="opacity-100 translate-y-0"
              leave-active-class="transition ease-in duration-150"
              leave-from-class="opacity-100 translate-y-0"
              leave-to-class="opacity-0 translate-y-1"
            >
              <PopoverPanel
                class="absolute z-10 left-1/2 transform -translate-x-1/2 mt-3 px-2 w-screen max-w-md sm:px-0"
              >
              </PopoverPanel>
            </transition>
          </Popover>
        </PopoverGroup>
        <div class="hidden md:flex items-center justify-end md:flex-1 lg:w-0">
          <!-- Dark mode toggle button; icon is moon during dark mode, sun during light mode -->
          <button
            class="ml-8 whitespace-nowrap inline-flex items-center justify-center px-4 py-3 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-gray-100 hover:bg-slate-900 dark:bg-slate-900 dark:hover:bg-gray-100"
            @click="switchTheme"
          >
            <MoonIcon
              :class="[
                open ? 'text-gray-600' : 'text-gray-400',
                'h-5 w-5 group-hover:text-gray-500',
              ]"
              v-if="darkMode"
              aria-hidden="true"
            />
            <SunIcon
              :class="[
                open ? 'text-gray-600' : 'text-gray-400',
                'h-5 w-5 group-hover:text-gray-500',
              ]"
              v-else
              aria-hidden="true"
            />
          </button>
          <button
            class="ml-8 whitespace-nowrap inline-flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-base font-bold text-white bg-blue-500 hover:bg-blue-700 dark:bg-blue-700 dark:hover:bg-blue-900"
            @click="goToLogin"
          >
            Sign in
          </button>
        </div>
      </div>
    </div>

    <transition
      enter-active-class="duration-200 ease-out"
      enter-from-class="opacity-0 scale-95"
      enter-to-class="opacity-100 scale-100"
      leave-active-class="duration-100 ease-in"
      leave-from-class="opacity-100 scale-100"
      leave-to-class="opacity-0 scale-95"
    >
      <PopoverPanel
        focus
        class="absolute top-0 inset-x-0 p-2 transition transform origin-top-right md:hidden"
      >
        <div
          class="rounded-lg shadow-lg ring-1 ring-black ring-opacity-5 bg-white dark:bg-gray-800 divide-y-2 divide-gray-50 dark:divide-gray-700"
        >
          <div class="pt-5 pb-6 px-5">
            <div class="flex items-center justify-between">
              <div>
                <button
                  class="whitespace-nowrap inline-flex items-center justify-center px-4 py-3 border border-transparent rounded-md shadow-sm text-base font-medium text-white bg-gray-100 hover:bg-slate-900 dark:bg-slate-900 dark:hover:bg-gray-100"
                  @click="switchTheme"
                >
                  <MoonIcon
                    :class="[
                      open ? 'text-gray-600' : 'text-gray-400',
                      'h-5 w-5 group-hover:text-gray-500',
                    ]"
                    v-if="darkMode"
                    aria-hidden="true"
                  />
                  <SunIcon
                    :class="[
                      open ? 'text-gray-600' : 'text-gray-400',
                      'h-5 w-5 group-hover:text-gray-500',
                    ]"
                    v-else
                    aria-hidden="true"
                  />
                </button>
              </div>
              <div class="-mr-2">
                <PopoverButton
                  class="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 dark:bg-slate-800 dark:hover:bg-gray-900 dark:hover:text-gray-300"
                >
                  <span class="sr-only">Close menu</span>
                  <XIcon class="h-6 w-6" aria-hidden="true" />
                </PopoverButton>
              </div>
            </div>
            <div class="mt-6">
              <nav class="grid gap-y-8">
                <div>
                  <Popover class="relative" v-slot="{ open }">
                    <PopoverButton
                      :class="[
                        open
                          ? 'text-gray-900 dark:text-gray-200'
                          : 'text-gray-500 dark:text-gray-400',
                        'group bg-white dark:bg-gray-800 rounded-md inline-flex items-center text-base font-medium hover:text-gray-900 dark:hover:text-gray-200',
                      ]"
                      @click="goToCourses"
                    >
                      <span>Search Courses</span>
                    </PopoverButton>
                  </Popover>
                  <div class="my-4">
                    <a
                      :href="repoUrl"
                      target="_blank"
                      class="text-base font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200"
                      >Docs</a
                    >
                  </div>
                  <div>
                    <a
                      href="#"
                      class="text-base font-medium text-gray-500 dark:text-gray-400 hover:text-gray-900 dark:hover:text-gray-200"
                      >About</a
                    >
                  </div>
                </div>
              </nav>
            </div>
          </div>
          <div class="py-4 px-5 space-y-6">
            <div>
              <p
                class="text-center text-base font-medium text-gray-500 dark:text-gray-400"
              >
                Existing user?
                {{ " " }}
                <button
                  class="text-indigo-600 hover:text-indigo-500 dark:text-indigo-500 dark:hover:text-indigo-600"
                  @click="goToLogin"
                >
                  Sign in
                </button>
              </p>
            </div>
          </div>
        </div>
      </PopoverPanel>
    </transition>
  </Popover>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import {
  Popover,
  PopoverButton,
  PopoverGroup,
  PopoverPanel,
} from "@headlessui/vue";
import { MenuIcon, MoonIcon, SunIcon, XIcon } from "@heroicons/vue/outline";
import { ChevronDownIcon } from "@heroicons/vue/solid";

// Toggle variable for turning dark mode on/off, theme persists between sessions
let darkMode = localStorage.getItem("user-theme") === "true";
if (darkMode) {
  document.documentElement.classList.add("dark");
}

export default defineComponent({
  name: "NavBar",
  components: {
    Popover,
    PopoverButton,
    PopoverGroup,
    PopoverPanel,
    ChevronDownIcon,
    MenuIcon,
    XIcon,
    MoonIcon,
    SunIcon,
  },
  data() {
    return {
      darkMode,
    };
  },
  methods: {
    goToLogin() {
      this.$router.push("/login");
    },
    goToMyCourses() {
      this.$router.push("/my-courses");
    },
    goToRegister() {
      this.$router.push("/register");
    },
    goToHome() {
      this.$router.push("/");
    },
    goToCourses() {
      this.$router.push("/course-search");
    },
    switchTheme() {
      // Switches the theme of the entire app, all routes
      if (document.documentElement.classList.contains("dark")) {
        document.documentElement.classList.remove("dark");
      } else {
        document.documentElement.classList.add("dark");
      }

      // For switching the dark mode button icon:
      this.darkMode = document.documentElement.classList.contains("dark");
      // Allows dark mode to persist between sessions:
      localStorage.setItem("user-theme", JSON.stringify(this.darkMode));
    },
  },
  setup() {
    return {
      repoUrl: "https://github.com/cs421sp22-homework/project-team-08-random",
    };
  },
  mounted() {
    // Ensures that switching views retains correct icon for dark mode toggle button
    this.darkMode = document.documentElement.classList.contains("dark");
  },
});
</script>