"use client"

import { useMainNews } from "@/hooks"
import Link from "next/link"

export const MainNews = () => {
    const { data, isLoading } = useMainNews()

    if (isLoading)
        return (
            <section>
                <div>loading....</div>
            </section>
        )

    return (
        <section>
            <ul>
                {data?.map((item, index) => (
                    <li key={index}>
                        <Link href={item.url}>{item.title}</Link>
                    </li>
                ))}
            </ul>
        </section>
    )
}
