self.addEventListener('install', function (e) {
    e.waitUntil(
        caches.open('projectsite-cache-v1').then(function (cache) {
            return cache.addAll([
                '/',
                '/static/css/bootstrap.min.css',
                '/static/js/core/bootstrap.min.js',
                '/static/js/core/popper.min.js',
                '/static/js/core/jquery.3.2.1.min.js',
                '/static/css/style.css',
                '/static/img/icon-512x512.png',
            ]);
        })
    );
});
self.addEventListener('fetch', function (e) {
    e.respondWith(
        caches.match(e.request).then(function (response) {
            return response || fetch(e.request);
        })
    );
});