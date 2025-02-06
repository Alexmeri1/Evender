// See https://svelte.dev/docs/kit/types#app.d.ts
// for information about these interfaces
declare global {
	namespace App {
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface PageState {}
		// interface Platform {}
	}

	interface TicketEventObject {
		city: string;
		country: string;
		date: string;
		event_name: string;
		info: string;
		price: number;
		url: string;
		venue: string;
	}
}


export {};
