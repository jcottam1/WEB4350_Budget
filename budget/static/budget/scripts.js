<script>
    // Timezone settings
    const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone; // e.g. "America/New_York"
    document.cookie = "django_timezone=" + timezone;
</script>