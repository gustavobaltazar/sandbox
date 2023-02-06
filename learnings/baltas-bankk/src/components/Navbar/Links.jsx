export const Links = ({ linkName = "Error", href="" }) => {
  return (
    <div className="py-2">
      <a className="hover:text-pink-500  md:visible lg:visible" href={href}>
        {linkName}
      </a>
    </div>
  );
};
