import type { ServerLoad } from '@sveltejs/kit';

export const load: ServerLoad = async ({ request }) => {
    const userAgent = request.headers.get('user-agent');
    let platform = 'unknown';

    if (userAgent) {
        if (/Mobi|Android/i.test(userAgent)) {
            platform = 'mobile';
        } else {
            platform = 'pc';
        }
    }

    let isMobile = platform != 'pc' ? true : false;
    // console.log(platform)
    // console.log(isMobile)
	return {
		isMobile
	};
};
