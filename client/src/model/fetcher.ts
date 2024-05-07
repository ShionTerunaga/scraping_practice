import { newsType } from "./types"

export const fetcher = async (url: string) => {
    const res = await fetch(url)

    const data = await res.json()

    return data as newsType[]
}
