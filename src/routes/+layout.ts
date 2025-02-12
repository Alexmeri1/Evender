
export function load({ data }: { data: { isMobile: boolean } }) {
    // console.log(data)
    return {
        isMobile: data.isMobile
    }
};